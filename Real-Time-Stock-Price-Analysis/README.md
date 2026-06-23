# 📈 Daily Stock Market Analysis Using PySpark

A scalable big data analytics project that leverages **PySpark** and the **Alpha Vantage API** to collect, process, and analyze historical stock market data for major technology companies. The project demonstrates data engineering, preprocessing, exploratory data analysis, and distributed computing techniques for financial datasets.

---

## 1. Project Overview

The primary objective of this project is to build a scalable stock market analytics pipeline capable of fetching, processing, and analyzing large volumes of historical stock data. By utilizing PySpark, the system efficiently handles financial datasets while performing data cleaning, integration, and statistical analysis.

---

## 2. Key Features

### Data Acquisition

* Automated stock market data collection using the Alpha Vantage API.
* Supports multiple stock symbols.
* Historical daily stock data retrieval.

### Distributed Data Processing

* Uses PySpark DataFrames for scalable data handling.
* Efficient processing of large historical datasets.
* Schema-based data validation and transformation.

### Data Integration

* Consolidates multiple stock datasets into a unified DataFrame.
* Enables cross-company comparative analysis.

### Exploratory Data Analysis

* Statistical outlier detection using IQR methodology.
* Distribution analysis through histograms and box plots.
* Volume and price trend analysis.

---

## 3. Workflow Summary

### Step 1: Data Ingestion

Historical stock data is collected for major technology companies:

* Apple (AAPL)
* Google (GOOG)
* Amazon (AMZN)
* Microsoft (MSFT)
* Tesla (TSLA)

### Step 2: Data Preprocessing

* Conversion of CSV/API data into PySpark DataFrames.
* Data type conversion for numerical attributes.
* Date parsing and formatting.
* Missing value validation.
* Data consistency checks.

### Step 3: Data Integration

* Merge datasets from multiple companies.
* Create a consolidated stock market dataset.

### Step 4: Outlier Analysis

* Interquartile Range (IQR) based outlier detection.
* Outlier capping for improved visualization and analysis.

---

## 4. Key Metrics

| Metric               | Value           |
| -------------------- | --------------- |
| Companies Analyzed   | 5               |
| Historical Range     | 1999 – 2025     |
| Dataset Size         | 25,000+ Records |
| Processing Framework | PySpark         |

---

## 5. Technologies Used

* Python
* PySpark
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Alpha Vantage API

---

## 6. Repository Structure

```text
Real-Time-Stock-Price-Analysis/
│
├── analysis.ipynb
├── stock_data.csv
└── README.md
```

---

## 7. Installation

### Install Dependencies

```bash
pip install pyspark pandas numpy matplotlib seaborn requests
```

### Configure Alpha Vantage API Key

Obtain a free API key from Alpha Vantage and configure it within the project.

### Run the Analysis

```bash
jupyter notebook
```

Open the notebook and execute the cells sequentially.

---

## 8. Applications

* Financial Data Analytics
* Stock Market Monitoring
* Big Data Processing
* Distributed Computing Research
* Investment Trend Analysis

---

## 9. Future Enhancements

* Real-Time Streaming with Apache Kafka
* Predictive Analytics using Machine Learning
* Interactive Dashboard using Streamlit
* Automated Portfolio Performance Monitoring

---

## Author

**P. Moksha**
B.Tech Computer Science Engineering (Artificial Intelligence)
