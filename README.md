
# 📈 Real-Time Stock Market Analysis

A scalable, end-to-end real-time data pipeline for ingesting, processing, and visualizing stock market data using modern data engineering tools.

---

## 🚀 Overview

This project demonstrates how to build a real-time streaming pipeline that:

* Extracts live stock data from the Vantage API
* Streams data using Apache Kafka
* Processes data in real time with Apache Spark
* Stores processed data in PostgreSQL
* Visualizes insights using Power BI

All components are containerized with Docker, making the system easy to deploy, scale, and reproduce across environments.

---

## 🏗️ Architecture

![Data Pipeline Architecture](./img/Data%20Pipeline%20Architecture%20(2).png)

---

## 🔄 Data Flow

1. **API Service** fetches real-time stock data from the Vantage API
2. Data is serialized as JSON and sent to Kafka topics
3. **Apache Kafka** acts as the streaming backbone
4. **Apache Spark** consumes data from Kafka and processes it
5. Processed data is written into **PostgreSQL**
6. **Power BI** connects to PostgreSQL for dashboards and analytics

---

## 🧰 Tech Stack

| Component    | Description                          |
| ------------ | ------------------------------------ |
| Apache Kafka | Distributed event streaming platform |
| Kafka UI     | Monitor Kafka topics and messages    |
| Apache Spark | Real-time data processing engine     |
| PostgreSQL   | Relational database for storage      |
| pgAdmin      | Database management interface        |
| Power BI     | Data visualization tool              |
| Docker       | Containerization platform            |

---

## 📦 Project Structure

```
.
├── api/                # Data ingestion service
├── spark/              # Spark streaming jobs
├── docker-compose.yml  # Service orchestration
├── img/                # Architecture diagrams
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/real-time-stock-analysis.git
cd real-time-stock-analysis
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory:

```env
API_KEY=your_vantage_api_key
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=stocks
```

### 3. Start Services with Docker

```bash
docker-compose up --build
```

This will start:

* Kafka & Zookeeper
* Kafka UI
* Spark
* PostgreSQL
* pgAdmin
* API producer service

---

## 🔍 Accessing Services

| Service    | URL                                            |
| ---------- | ---------------------------------------------- |
| Kafka UI   | [http://localhost:8080](http://localhost:8080) |
| pgAdmin    | [http://localhost:5050](http://localhost:5050) |
| PostgreSQL | localhost:5432                                 |

---

## 📊 Connecting Power BI

1. Open Power BI
2. Select **Get Data → PostgreSQL**
3. Enter connection details:

   * Server: `localhost`
   * Database: `stocks`
4. Load tables and build dashboards

---

## 🧪 Example Use Cases

* Real-time stock price monitoring
* Trend analysis and aggregation
* Financial data dashboards
* Streaming data engineering practice

---

## 🛠️ Future Improvements

* Add data validation and schema enforcement
* Implement alerting for stock thresholds
* Integrate machine learning for predictions
* Deploy to cloud (AWS/GCP/Azure)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Acknowledgements

* Apache Kafka
* Apache Spark
* PostgreSQL
* Docker

 