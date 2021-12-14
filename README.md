# zeebe-message-aggregator
A concrete and working example of Zeebe's documented 'Message aggregator' flow
![bpmn](https://docs.camunda.io/assets/images/message-aggregator-1dbf88f6e2c7145aa238721cbf3570f1.png)

It's unclear if this is the best practice way of doing things.
Details of note

* Created messages must include a copy of the correlation_key in the variables section of the message
* The Start Message event puts the content of the message into a List (i.e. messages)
* The Intermediate Message event appends a message with same the correlation key (ck) as the first (i.e. messages) 
* An Exclusive Gateway will loop back if the length (count) of the list is less than X (3 is used for testing)
* One the List grows to a sufficient size (3), a Script Task is executed for the entire list


## Try for yourself
```
docker-compose build
docker-compose up

...
...
test_1   | start
test_1   | deploy processes
test_1   | send messages
test_1   | send message 1 of 20
test_1   | send message 2 of 20
test_1   | send message 3 of 20
test_1   | send message 4 of 20
test_1   | send message 5 of 20
test_1   | send message 6 of 20
test_1   | send message 7 of 20
test_1   | send message 8 of 20
test_1   | send message 9 of 20
test_1   | send message 10 of 20
test_1   | send message 11 of 20
test_1   | send message 12 of 20
test_1   | send message 13 of 20
test_1   | send message 14 of 20
test_1   | send message 15 of 20
test_1   | buffered ['iteration #00 ck0 2021-12-14 03:57:37.222862', 'iteration #03 ck0 2021-12-14 03:57:38.069560', 'iteration #06 ck0 2021-12-14 03:57:39.753560']
test_1   | send message 16 of 20
test_1   | buffered ['iteration #01 ck1 2021-12-14 03:57:37.553215', 'iteration #04 ck1 2021-12-14 03:57:38.458341', 'iteration #07 ck1 2021-12-14 03:57:40.332719']
test_1   | buffered ['iteration #02 ck2 2021-12-14 03:57:37.783867', 'iteration #05 ck2 2021-12-14 03:57:38.960581', 'iteration #08 ck2 2021-12-14 03:57:40.914448']
test_1   | send message 17 of 20
test_1   | send message 18 of 20
test_1   | send message 19 of 20
test_1   | send message 20 of 20
test_1   | buffered ['iteration #09 ck0 2021-12-14 03:57:41.449513', 'iteration #12 ck0 2021-12-14 03:57:43.114698', 'iteration #15 ck0 2021-12-14 03:57:44.929331']
test_1   | buffered ['iteration #10 ck1 2021-12-14 03:57:41.921731', 'iteration #13 ck1 2021-12-14 03:57:43.641129', 'iteration #16 ck1 2021-12-14 03:57:45.446048']
test_1   | buffered ['iteration #11 ck2 2021-12-14 03:57:42.482747', 'iteration #14 ck2 2021-12-14 03:57:44.304427', 'iteration #17 ck2 2021-12-14 03:57:45.972380']
...
```
