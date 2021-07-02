# Automatic Startup of a Kafka environment

#### Perform a gitpull on the repository
> 1. Pull the repository from github by executing the following command: `git clone https://github.com/ioksmio/KES.git`
> 2. Create a directory under /home/vm/Downloads/kafka_2.12-2.8.0 named `docker-compose`
> 3. Navigate to /home/vm/Downloads/kafka_2.12-2.8.0/docker-compose and execute the following command: `cp /vm/KES/Session01/03_start-kafka-docker-compose.yml.`
> 4. Start the Kafka environment by executing the following command: `docker-compose -f 03_start-kafka-docker-compose.yml up`
> 5. Check whether there is a binding to the port 2181
> 6. Check whether the Server has started properly by checking the id of the Kafka Server
