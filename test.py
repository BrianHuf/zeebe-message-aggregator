import asyncio
import logging
from datetime import datetime
from typing import List
from pyzeebe import ZeebeClient, ZeebeWorker, create_insecure_channel
from time import sleep

logging.basicConfig(format='%(message)s')
log = logging.getLogger('example')
log.setLevel("INFO")

# wait for zeebe to warm up
sleep(5)


log.info("start")
grpc_channel = create_insecure_channel(hostname="zeebe", port=26500)
worker = ZeebeWorker(grpc_channel)
client = ZeebeClient(grpc_channel)


@worker.task(task_type='unbuffered')
def unbuffered(message: str):
    log.info("unbuffered %s", message)


@worker.task(task_type='buffered')
def buffered(messages: List[str]):
    log.info("buffered %s", messages)


async def test():
    log.info("deploy processes")
    await client.deploy_process('consume_buffered.bpmn')
    await client.deploy_process('consume_unbuffered.bpmn')

    log.info("send messages")
    NUM = 20
    correlation_key = 'ck1'

    for i in range(NUM):
        await asyncio.sleep(0.1)
        log.info("send message %s of %s", i+1, NUM)
        await client.publish_message(name='test', correlation_key=correlation_key, variables={
            'message': f'iteration #{i} at {datetime.now()}',
            'correlation_key': correlation_key,
        })


async def main():
    await asyncio.gather(
        worker.work(),
        test()
    )


asyncio.get_event_loop().run_until_complete(
    main()
)
