# zeebe-message-aggregator
A concrete and working example of Zeebe's documented 'Message aggregator' flow
![bpmn](https://docs.camunda.io/assets/images/message-aggregator-1dbf88f6e2c7145aa238721cbf3570f1.png)

It's unclear if this is the best practice way of doing things.
Details of note

* Created messages must include a copy of the correlation_key in the variables section of the message
* The Start Message event puts the content of the message into a List (i.e. messages)
* The Intermediate Message event appends a message into a List (i.e. messages)
* An Exclusive Gateway will loop back if the length (count) of the list is less than X (3 is used for testing)
* One the List grows to a sufficient size (3), a Script Task is executed for the entire list


NOTE: an unbuffered process is running in parallel for purposes of testing

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
test_1   | unbuffered iteration #0 at 2021-12-14 02:50:45.136124
test_1   | send message 6 of 20
test_1   | send message 7 of 20
test_1   | send message 8 of 20
test_1   | send message 9 of 20
test_1   | send message 10 of 20
test_1   | send message 11 of 20
test_1   | send message 12 of 20
test_1   | send message 13 of 20
test_1   | unbuffered iteration #1 at 2021-12-14 02:50:45.419802
test_1   | send message 14 of 20
test_1   | send message 15 of 20
test_1   | send message 16 of 20
test_1   | buffered ['iteration #0 at 2021-12-14 02:50:45.136124', 'iteration #1 at 2021-12-14 02:50:45.419802', 'iteration #2 at 2021-12-14 02:50:45.826908']
test_1   | send message 17 of 20
test_1   | send message 18 of 20
test_1   | send message 19 of 20
test_1   | send message 20 of 20
test_1   | unbuffered iteration #2 at 2021-12-14 02:50:45.826908
test_1   | unbuffered iteration #3 at 2021-12-14 02:50:46.156773
test_1   | buffered ['iteration #3 at 2021-12-14 02:50:46.156773', 'iteration #4 at 2021-12-14 02:50:46.443655', 'iteration #5 at 2021-12-14 02:50:46.824981']
test_1   | unbuffered iteration #4 at 2021-12-14 02:50:46.443655
test_1   | unbuffered iteration #5 at 2021-12-14 02:50:46.824981
test_1   | unbuffered iteration #6 at 2021-12-14 02:50:47.265940
test_1   | buffered ['iteration #6 at 2021-12-14 02:50:47.265940', 'iteration #7 at 2021-12-14 02:50:47.677557', 'iteration #8 at 2021-12-14 02:50:48.014095']
...
```
