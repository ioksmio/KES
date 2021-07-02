# Demo Kafka Setup

### 1. Download Kafka binaries

> Download Kafka at https://kafka.apache.org/downloads

### 2. Extract Kafka
```
tar -xvf kafka_2.12-2.8.0.tgz
```

### 3. Navigate to the Kafka directory
```
cd /home/vm/Downloads/kafka_2.12-2.8.0
```

### 4. this should show JDK 8
```
java -version 
```

### 5. Otherwise Install Java JDK 8 (must be 8!)
```
sudo apt install -y openjdk-8-jdk
```
> If prompted for a password enter: "vm010101"
### 6. Verify Java 8 version
```
java -version
```
### 7. Try out a Kafka command
```
bin/kafka-topics.sh
```

### 8.  We shall now edit append a new path to the existing path file by editing .bashrc in the home folder

> 1. Run the command `nano ~/.bashrc`
> 2. Go to the bottom of the file an add the following line: `export PATH=/home/vm/Downloads/kafka_2.12-2.8.0/bin:$PATH`
> 3. Save the file

### 9. Test whether your changes were successful 
> 1. Open a new terminal
> 2. Run the following command

```
kafka-topics.sh
```

