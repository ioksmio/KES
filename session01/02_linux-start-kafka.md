# Start Kafka involves the following two steps
> 1. Starting the Zookeeper Server
> 2. Starting the Kafka Server 

#### Create a folder named data and a subfolder named zookeeper 
The folder to be created will hold data for Zookeeper. Your folder structure should look like this: `/home/vm/Downloads/kafka_2.12-2.8.0/data/zookeeper`
> 1. Navigate to /home/vm/Downloads/kafka_2.12-2.8.0 and execute the following command: `mkdir data`
> 2. Navigate to /home/vm/Downloads/kafka_2.12-2.8.0/data and execute the following command: `mkdir zookeeper`


#### So that the Zookeeper folder can be utilized we need to set the correct path in the respective the properties file
> 1. Navigate to /home/vm/Downloads/kafka_2.12-2.8.0/config and execute the following command `nano zookeeper.properties`
> 2. Look for dataDir and change it to the following line: `dataDir=/home/vm/Downloads/kafka_2.12-2.8.0/data/zookeeper`
> 3. Save the file 
> 4. Check whether the enty has been saved appropriately by executing the following command: `cat /home/vm/Downloads/kafka_2.12-2.8.0/config/zookeeper.properties | grep dataDir`

#### Steps for starting the Zookeeper Server
To start the server you need to specify the location of the properties file.
> 1. Execute the following Command `zookeeper-server-start.sh ../config/zookeeper.properties`
> 2. Check whether there is a binding to the port 2181
> 3. Navigate to  /home/vm/Downloads/kafka_2.12-2.8.0/data/zookeeper and check whether a new folder has been created. 
> 

#### Steps for starting the Kafka Server
 > 1. Navigate to /home/vm/Downloads/kafka_2.12-2.8.0/data
 > 2. Create a folder named kafka by executing the following command: `mkdir kafka`
 > 3. Navigate to /home/vm/Downloads/kafka_2.12-2.8.0/config and execute the following command `nano server.properties`
 > 4. Search for the setting log.dirs=/tmp/kafka-logs and change it to `log.dirs=/home/vm/Downloads/kafka_2.12-2.8.0/data/kafka` 
 > 5. Check whether the entry has been saved appropriately by executing the following command: `cat /home/vm/Downloads/kafka_2.12-2.8.0/config/server.properties | grep log.dirs`
 > 6. Start the Kafka Server by executing the following command: `kafka-server-start.sh ../config/server.properties`
 > 7. Check whether the Server has started properly by checking the id of the Kafka Server
 > 8. Navigate to /home/vm/Downloads/kafka_2.12-2.8.0/data/kafka and check whether there are any new files that have been created
 > 9. Keep the two terminals open.
 > 10. Stop the Kafka Server `kafka-server-stop.sh`and the zookeeper server `zookeeper-server-stop.sh`
