FROM python:3.9-slim

RUN pip install pyzeebe==3.0.0

ADD test.py consume_buffered.bpmn /

CMD ["python", "test.py"]
