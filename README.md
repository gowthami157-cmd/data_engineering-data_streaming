# data_engineering-data_streaming
🚧 Work in Progress

This environment is currently being set up as part of a full data-engineering pipeline. The core infrastructure is now up and running, and the next steps will focus on building out the streaming workflows, Spark jobs, and Airflow orchestration.

✔ What’s been completed so far

Docker-based data engineering stack configured and launched, including Kafka, Zookeeper, Schema Registry, Control Center, Airflow, Postgres, Cassandra, and Spark.

Replaced deprecated Bitnami Spark images with the official apache/spark:3.5.1 images and fixed startup commands to match Apache’s directory structure.

Resolved Airflow initialization issues by manually running database migrations (airflow db init + airflow db upgrade), ensuring the webserver and scheduler start cleanly.

Verified all services are healthy, with Spark master/worker running, Kafka broker active, Control Center accessible, Airflow UI live, and Cassandra ready for writes.

The system is now ready for developing pipelines, such as Kafka → Spark Streaming → Cassandra, and Airflow-driven batch/stream workflows.