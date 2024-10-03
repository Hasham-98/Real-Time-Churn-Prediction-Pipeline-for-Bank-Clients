## The Real-Time Churn Prediction Pipeline for Bank Clients 

My Graduation Project at the Information Technology Institute (ITI) Data Engineering Track
The project is designed to process and analyze banking customer data to predict customer churn in real-time using a robust data streaming architecture. 
The pipeline integrates various modern technologies to ingest, process, and visualize the data efficiently.

### Pipeline Components:

1. Data Ingestion (Python Script):

The pipeline begins with a Python script responsible for reading the Bank dataset. This dataset contains essential client information necessary for analyzing churn behavior.
The data is ingested and streamed into the pipeline via a Kafka cluster for real-time processing.

2. Kafka Cluster:
   
The ingested data is then streamed into an Apache Kafka cluster. Kafka handles the streaming data in real time and makes it available to downstream consumers.
Kafka acts as a messaging layer, ensuring continuous and scalable data flow.

3. Apache Spark (Streaming & Machine Learning):

Apache Spark is employed to stream data from the Kafka cluster and perform real-time processing.
Spark runs machine learning models to predict whether a client is at risk of churn based on historical data and behavioral patterns.
The predictions are exported and stored for further analysis.

4. Amazon S3 (Data Storage):

The processed data and the results of the churn prediction model are saved into an Amazon S3 bucket.
This enables scalable storage and easy access to the prediction results for other applications or users.

5. Airflow (Orchestration):

Apache Airflow is used for orchestration and scheduling within the pipeline.
It deploys and triggers DAGs (Directed Acyclic Graphs) to ensure the automation of tasks such as data ingestion, processing, and exporting.
Airflow schedules jobs for periodic data processing and the maintenance of the streaming pipeline.

6. Power BI (Data Visualization):

Power BI is connected to the output data stored in Amazon S3.
It retrieves the prediction results and creates real-time dashboards for business users and analysts to monitor client churn patterns.
This visualization helps stakeholders make data-driven decisions on customer retention strategies.

### Technology Stack:

- Data Ingestion & Streaming: Python, Apache Kafka
- Data Processing & Machine Learning: Apache Spark
- Data Storage: Amazon S3
- Orchestration: Apache Airflow
- Visualization: Power BI
- Deployment Environment: Docker (Containerized services for portability and ease of deployment)


In summary, this real-time churn prediction pipeline enables the bank to continuously monitor and analyze customer data, 
identifying potential churn cases before they happen. The combination of streaming, machine learning, 
and visualization allows for rapid and actionable insights into client behaviors.
