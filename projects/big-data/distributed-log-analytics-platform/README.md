# Distributed logs & analytics platform


## Overview
In this repo I will be learning how to correctly set up and use things like logstash, elastic search, kibana and kafka.
This repo will be set public for people to see and learn so please don't mind the mess, I'm still eagerly learning myself!

## Architecture

## Technologies Used
Before starting I'll go over the technology used and what it does and stuff.

### Log Generator Service
This simulates:

* backend APIs
* microservices
* production applications

It will:

* emit structured JSON logs
* generate INFO/WARN/ERROR logs
* simulate traffic

Example:

```code

{

  "timestamp": "2026-05-12T10:15:00",

  "service": "auth-service",

  "level": "ERROR",

  "message": "Database connection timeout",

  "user_id": 1024

}
```
I understand this is MUCH better than plain text logs.

### Filebeat
Role:

* lightweight log shipper
* tails log files
* forwards events to Kafka

### Kafka
Role:

* distributed event buffer
* decouples ingestion from processing
* prevents pipeline overload

Apparently loved.

#### Logstash
Role:

* consumes Kafka messages
* parses/transforms data
* enriches events
* forwards to Elasticsearch

### Elasticsearch
Role:

* distributed search/indexing engine

search engine ? 

### Kibana
Role:

* dashboards
* visualizations
* observability UI

No need to build frontend. Thank God.

### Apache Zookeeper
A distributed coordination system. In theory it should help systems by saying who is leader, who is alive, cluster coordination and so on. Seems like Kafka needs it.

## Steps

Left foot, right foot, left foot, ri-...

- Started with setting up [docker-compose.yaml](docker-compose.yml) 

notes : Does order of services matter ? Yes very much, due to dependencies. For example Kafka cannot start before ZooKeeper. We use things like 'Depends_on' to make sure the whole soup doesn't crash.

- Set up log-generator inside the [Dockerfile](./services/log-generator/Dockerfile) (that thing that feeds the pipeline)
- Need a way to generate realistic logs, hence [app.py](./services/log-generator/app.py)
```code
docker compose up --build
```
### Filebeat and Kafka
- Now we gotta wire Filebeat to Kafka. Kafka needs topics
```code
docker exec -it kafka bash

kafka-topics \
--create \
--topic application-logs \
--bootstrap-server localhost:9092

kafka-topics \
--list \
--bootstrap-server localhost:9092
----exit----
exit
```
- configure [Filebeat](./filebeat/filebeat.yml). Now Filebeat should ship new log entries to Kafka.
```code
docker compose restart filebeat
````
- verify messages reach kafka
```code
docker exec -it kafka bash

kafka-console-consumer \
--topic application-logs \
--bootstrap-server localhost:9092 \
--from-beginning

```
### Creating a Logstash Pipeline
- Let's start with [pipeline.conf](./logstash/pipeline/pipeline.conf). We'll set it to filter certain events.
```code
docker compose restart logstash

docker logs -f logstash
```
- Also, you should see Elasticsearch info in JSON with http://localhost:9200
- With http://localhost:9200/_cat/indices?v you can see the index.

### Kibana
- if the ochestration gods are by your side http://localhost:5601 should display Kibana.

## Usefull commands
Some commands I thought were handy.

- Start stack ```docker compose up -d```

- Stop stack ```docker compose down```

- Stop + remove volumes (WARNING: deletes Elasticsearch data) ```docker compose down -v```

- Rebuild containers after code/config changes ```docker compose up --build -d```

- View logs```docker compose logs -f```

    or ```docker logs -f logstash```

## Infrastructure
## Setup & Deployment
## Screenshots
## Lessons Learned
## Future Improvements