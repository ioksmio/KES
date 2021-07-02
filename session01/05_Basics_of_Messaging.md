## 1. Working with the CLI is very important to understanding Kafka. In this execise we shall:
> 1. Get a basic understanding of the CLI
> 2. Create Topics
> 3. Work with the Producer CLI
> 4. Get an understanding of Consumer Groups
> 5. Reset Offsets 

#### 1.1 Start your Kafka-Setup with a docker-compose file.
> 1. Since we are running in a docker environment we shall connect with a container and execute our commands from within a container. Please use the docker-compose.yml, if not already done so in the previous excercise, to initiate your environment by executing the following command: `docker-compose -f kafka-kafka_manager-zookeeper.yml up`
> 2. Check whether the following containers: `zookeeper`, `kafka-manager` and `kafka` are up and running by execting the following command: `docker container ls -a`
```
CONTAINER ID   IMAGE                            COMMAND                  CREATED       STATUS       PORTS                                                                     NAMES
b76ebcd04d21   zookeeper                        "/docker-entrypoint.…"   2 hours ago   Up 2 hours   2888/tcp, 3888/tcp, 0.0.0.0:2181->2181/tcp, :::2181->2181/tcp, 8080/tcp   zookeeper
b95a7df2f264   wurstmeister/kafka               "start-kafka.sh"         2 hours ago   Up 2 hours   0.0.0.0:9092->9092/tcp, :::9092->9092/tcp                                 kafka
30470e7ee679   hlebalbau/kafka-manager:stable   "/kafka-manager/bin/…"   2 hours ago   Up 2 hours   0.0.0.0:9000->9000/tcp, :::9000->9000/tcp                                 kakfa-manager
```
3 containers should be depicted as shown above
 

#### 1.2 Get an understanding of how kafka-cli works


> 1. Execute the following command to access the kafka container `docker container exec -it kafka bash`
> 2. Execute the command: `kafka-topics.sh`
With this command you are able to see all options that can be passed onto the Kafka-Server as well as the REQUIRED options (when ommitted the command will not be executed)

#### 1.3 Create a topic named first_topic
> 1. Create a topic by executing the following command `kafka-topics.sh --create --zookeeper zookeeper --topic first_topic --partitions 3 --replication-factor 1` Were you able to create a topic?
> 2. Once you have managed to create your topic, check whether your it will be enlsited with the following command: `kafka-topics.sh --zookeeper zookeeper:2181 --list`
This command shows a list of all topics that have been created


#### 1.4 Check the specifications of a particular topic
> Execute the command: `kafka-topics.sh --zookeeper zookeeper:2181 --topic first_topic --describe` to check the name of the topic, the number of partitions, the replication factor defined, and other configurations

#### 1.5 Delete a topic
> 1. Create a second topic with the name second_topic
> 2. Enlist the topics you have created, if everything went well you should be having two topics enlisted
> 3. Delete the topic by executing the following command: `kafka-topics.sh --zookeeper  zookeeper:2181 --topic second_topic --delete`
> 4. Check whether `second_topic` has been deleted by enlisting all the topics. Execute the follwing command: `kafka-topics.sh --zookeeper zookeeper:2181 --list`

## 2. Sending Data to Kafka through the kafka-console-producer command line

#### 2.1 Get Access to the command options 
Execute the following command: `kafka-console-producer.sh`. You will see that 2 options are REQUIRED: `bootstrap-server` and `topic`

#### 2.2 Send a message to first_topic
> 1. Execute the following command:`kafka-console-producer.sh --bootstrap-server kafka:9092 --topic first_topic`
> 2. Once the '>' sign appears enter a message of your choice, when done, hit enter. Do this for four times.
> 3. Hit `CTRL-C` and you will return to your bash prompt

#### 2.3 Create Messages with assured transmissions through acks
1. Execute the following command:`kafka-console-producer.sh --bootstrap-server kafka:9092 --topic first_topic --producer-property acks=all`. This will impose acks from leader and replica partitions
> 2. Once the '>' sign appears enter a message of your choice, when done, hit enter. Do this for four times.
> 3. Hit `CTRL-C` and you will return to your bash prompt

#### 2.4 New topics that are created the first time will throw an error with the first message created
> 1. Execute the following command `kafka-console-producer.sh --bootstrap-server kafka:9092 --topic new_magenta`
> 2. Enter a message of your choice and hit `Enter`. What message do you get ? Could you possibly enter another message?
> 3. Hit `CTRL-C` and you will return to your bash prompt
> 4. Enlist your current topics by executing:`kafka-topics.sh --zookeeper zookeeper:2181 --list`
> 5. Check how many partitions and the replication factor new_magenta has by executing the following command `kafka-topics.sh --zookeeper zookeeper:2181 --describe`
What was the error message that was produced?


#### 2.5 Increase the number of partitions by editing the server.properties file
By default the number of partions created is one. This behaviour can be changed by editing the server.properties file to a standard of your desire
> 1. Navigate to `/opt/kafka/config`
> 2. Execute `vi server.properties`
> 3. Navigate to the line 65 (num.partitions=1) and change `num.partionts=3` by hitting `i` and changing the number of partitions to 3
> 4. Hit the `ESC` button and then enter `:` in the prompt followed by `wq!` to save changes to the server.properties file
> 5. Check whether the changes were saved by executing the following command: `cat server.properties | grep num.partitions` 
> 6. Exit the container by entering `exit` into the prompt
> 7. Restart the Kafka environment by executing `docker-compose -f kafka-kafka_manager-zookeeper.yml restart`
> 8. Execute the following command to access the kafka container `docker container exec -it kafka bash`
> 9. Add a new topic by executing the following command: `kafka-console-producer.sh --bootstrap-server kafka:9092 --topic new_new_magenta` 
> 10. Add four new messages and hit `CTRL-C`
> 11. Check whether the new topic `new_new_magenta` has been created and check the number of desired partitions by executing the following command `kafka-topics.sh --zookeeper zookeeper:2181 --topic new_new_magenta --describe`. How many partitions were created?

## 3. Verify that data was sent to Kafka with the kafka-console-consumer command 

#### 3.1 Get Access to the command options 
Execute the following command: `kafka-console-consumer.sh`. You will be presented with all the options of which the `bootstrap-server` is the most important and thus therequired option.

#### 3.2 Receive a message on a topic 
> 1. Execute the following command:`kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic first_topic`. Expect the command prompt to stall(it is now in the consumer mode).Although messages were sent to this topic earlier they are not shown, only when you send further messages, can they be consumed by the consumer.
> 2.   Execute the following command:`kafka-console-producer.sh --bootstrap-server kafka:9092 --topic first_topic` in a second terminal and observe how the messages are received by the consumer
> 3. To consume messages from the beginning execute the following command: `kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic first_topic --from-beginning`. Messages from the beginning will be presented. However, their order will be different to how they were entered. This is because order is only guaranteed at partition level

## 4. Working with Consumer groups and Offsets

#### 4.1 Functionality of Consumer Groups
In this section we will see how consumer groups work. First we will start with two terminals, where one terminal will be the producer and the second the consumer. Then we shall gradually add two other consumers and see how the messages are conumed within a consumer group.

> 1. Start the first terminal (our producer) and execute the following command: `kafka-console-producer.sh --bootstrap-server kafka:9092 --topic first_topic`
> 2. Start a second terminal (our first consumer in a consumer group) and execute:`docker container exec -it kafka bash` to enter the container and then execute: `kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic first_topic --group App-One`
> 3. Post three new messages
> 4. Start a third terminal (our second consumer in a consumer group) and execute:`docker container exec -it kafka bash` to enter the container and then execute: `kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic first_topic --group App-One`
> 5. Post another three messages and observe how the consumer groups splitt the receiving of the messages. What do you observe
> 6. Start a fourth terminal (our third consumer in a consumer group) and execute:`docker container exec -it kafka bash` to enter the container and then execute: `kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic first_topic --group App-One` 
> 7. Post another three messages and observe how the messages are balanced between the consumers
 > 8. Stop the third consumer by executing `CTRL-C` and continue posting messages. Is there a redistribution of the messages?
 > 9. Stop the other two consumers by executing `CTRL-C` in each respective terminal


#### 4.2 Consumer groups and offsets
Offsets are committed by the consumer after data has been processed. To demonstrate how this works perform the following:
> 1. Create a new group named `App-Two` and have it read from `first_topic` from the beginning by executing the following command:`kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic first_topic --group App-Two --from-beginning`. This will display all messages. 
> 2. Stop the consumer and execute `kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic first_topic --group App-Two --from-beginning` a second time. This time there are no more messages. The offset has been set because all messages have been processed by App-Two and thus an offset has been commited to Kafka
> 3. Post new 3 new messages. Stop the consumer by hitting `CTRL-C`. 
> 4. Post another 3 new messages. Restart the consumer with the following command: `kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic first_topic --group App-Two --from-beginning`. How many new messages can you see?
> 5. Stop the producer and the consumer by executing `CTRL-C` in each respective terminal
#### 4.3  Working with kafka-consumer-groups 

#### Enlist the consumer groups currently present and obtain various information on usage etc.
> 1. Execute `kafka-consumer-groups.sh --bootstrap-server kafka:9092 --list`, will enlist all consumer groups defined
> 2. Execute `kafka-consumer-groups.sh --bootstrap-server kafka:9092 --describe --group App-One` to obtain more information on a particular consumer group, i.e., active members, offset per partition etc.
Which options are REQUIRED and which options are optional?

#### 4.4 Reset Offsets to reread already processed data
Using `kafka-consumer-groups` allows for the resetting of offsets with the use of different options such as `--reset offsets` 
#### Reset offset to earliest by a certain topic
> 1. Execute the following command `kafka-consumer-groups.sh --bootstrap-server kafka:9092 --group App-One --reset-offsets --to-earliest  --topic first_topic` to reset the offset to 0. Did it work? What was missing?
> 2.  Check whether you can read all the messages that were sent to the topic by executing the following command:`kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic first_topic --group App-One` 
