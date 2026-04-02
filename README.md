# Project Name: Real Time Stock Market Analysis

The project implements a real-time data pipline that extracts stock data from ventage API, STREAMS IT THROUGH Apache Kafka, processes it with Apache Spark, and loads it into a postgres database. 

All components are containerized with Docker for easy deployment

### Data Pipeline Architecture
![The Design of Data Pipeline Architecture](./img/Data%20Pipeline%20Architecture%20(2).png)


Project Tech Stack and Flow

- `Kafka UI -> inspect topics/messages.`
- `API -> produces JSON events into Kafka.`
- `Spark -> consumes from kafka, writes to postgres.`
- `Postgres -> stores results for analytics.`
- `pgAdmin -> manage Postgres visually.`
- `Power BI -> external (connects to Postgres Database).`
 