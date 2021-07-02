## Displaying Kafka Monitoring Data in Grafana
In this exercise you shall set up an environment, where you are able to monitor your local  kafka instance and display the monitoring data in Grafana.  It is expected that all of you will be able to depict the monitoring data of their instance within Grafana.

Before you start with this exercise make sure that no container instances are up and running. You may use `docker kill zookeeper kafka kakfa-manager`  followed by `docker rm zookeeper kafka and kakfa-manager` to clean your working environment.

The main steps you need to accomplish are:
> 1. You will need to install and setup prometheus
> 2. You will need to download and install the JMX Exporter Agent as well as the Kafka configuration file so that it can expose Kafka's monitoring data. Please go to the following site to obtain the two files:  https://github.com/prometheus/jmx_exporter/tree/master/example_config
> 3. You will need to instanciate grafana, define the data source and import a kafka dashboard from the grafana website.