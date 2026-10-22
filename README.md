# 📦 Retail Inventory Optimization

### A Business Analytics Dashboard for Retail Sales, Demand Forecasting, and Inventory Risk Monitoring

## 📌 Project Overview

Retail businesses must maintain the right inventory levels to meet customer demand while minimizing excess stock and potential stockouts. Poor inventory management can lead to lost sales, unnecessary holding costs, and inefficient purchasing decisions.

This project uses data analytics and an interactive dashboard to explore retail sales performance, monitor inventory levels, evaluate demand forecast errors, and identify potential inventory risks.

The objective is to transform raw retail data into actionable business insights that can support better inventory planning and data-driven decision-making.

## 🎯 Business Objectives

- Analyze sales performance across product categories, stores, and products.
- Monitor inventory levels and estimated sales revenue.
- Evaluate the accuracy of demand forecasts.
- Identify records that may indicate potential stockout or overstock risks.
- Build an interactive dashboard for exploring retail performance.
- Support data-driven inventory management and replenishment decisions.

## 📊 Dataset

The project uses the **Retail Store Inventory Forecasting Dataset** from Kaggle.

- **Source:** [Retail Store Inventory Forecasting Dataset](https://www.kaggle.com/datasets/anirudhchauhan/retail-store-inventory-forecasting-dataset)
- **Number of records:** 73,100
- **Number of features:** 15
- **Coverage:** 5 stores and 20 products
- **Data frequency:** Daily retail records

The dataset includes information about dates, stores, products, categories, regions, inventory levels, units sold, units ordered, demand forecasts, prices, discounts, promotions, competitor pricing, weather conditions, and seasonality.

*Note: The dataset is synthetic and is intended for analytical and educational purposes.*

## 🛠️ Tools & Technologies

- **Python** — Data analysis and calculations
- **Pandas** — Data cleaning and transformation
- **Streamlit** — Interactive dashboard development
- **Plotly** — Interactive data visualizations
- **Google Colab** — Exploratory data analysis and development
- **GitHub** — Version control and project documentation
- **Streamlit Community Cloud** — Application deployment

## 🔍 Data Analysis & Feature Engineering

The analysis includes:

1. Data quality checks, including missing values, duplicate records, and date validation.
2. Calculation of estimated revenue using units sold and unit price.
3. Calculation of absolute demand forecast error.
4. Calculation of an inventory-to-forecast coverage indicator.
5. Aggregation of sales and inventory metrics by category and product.
6. Preliminary screening for potential stockout and overstock conditions.

### Key Metrics

| Metric | Description |
|---|---|
| Total Units Sold | Total quantity sold across the selected records |
| Estimated Revenue | Units sold multiplied by unit price |
| Average Inventory Level | Average recorded inventory quantity |
| Mean Absolute Forecast Error | Average absolute difference between units sold and demand forecast |
| Potential Stockout Records | Records with less than one day of forecast demand in stock |
| Potential Overstock Records | Records with more than three days of forecast demand in stock |

The stock coverage thresholds are illustrative screening rules, not validated operational standards. The forecast error metric is a simple comparison of units sold and demand forecast; it does not establish forecast accuracy against actual future demand.

## 📈 Dashboard Features

The Streamlit application provides:

- **Interactive filters:** Filter by product category, store, and date range.
- **KPI cards:** View units sold, estimated revenue, average inventory, and mean forecast error.
- **Category performance:** Compare estimated revenue and units sold across categories.
- **Top product analysis:** Identify the top 10 products by estimated revenue.
- **Inventory coverage analysis:** Explore average stock coverage by category.
- **Inventory risk overview:** Monitor records flagged for potential stockouts or overstock.
- **Data table:** Explore the underlying inventory records.
- **CSV export:** Download filtered inventory data for further analysis.

## 💡 Business Value

This project demonstrates how business analytics can help retail teams:

- Identify high-performing products and categories.
- Improve visibility into sales and inventory patterns.
- Investigate possible mismatches between inventory and forecast demand.
- Prioritize further investigation of potential stock risks.
- Support purchasing, replenishment, and inventory planning discussions.

The dashboard provides analytical decision support. Its risk indicators should be validated against actual lead times, service-level targets, and business rules before being used operationally.

## 🚀 Live Dashboard

**Explore the interactive application:** [Retail Inventory Optimization Dashboard](ADD_YOUR_STREAMLIT_APP_URL_HERE)

## 📁 Project Structure

```text
retail-inventory-optimization/
│
├── app.py
├── retail_inventory.csv
├── requirements.txt
└── README.md
```

## ⚙️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/retail-inventory-optimization.git
cd retail-inventory-optimization
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the dashboard

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔮 Future Improvements

- Implement time-series forecasting to predict future product demand.
- Develop data-driven reorder point and safety stock recommendations.
- Incorporate supplier lead times and inventory holding costs.
- Add inventory turnover and service-level metrics using appropriate historical data.
- Evaluate forecast performance using MAE, RMSE, and other suitable metrics.
- Introduce automated alerts for inventory risks.
- Test replenishment policies against historical demand.

## 👤 Author

**Leny NYMBUSSEDE  NAPALA**

This project demonstrates practical skills in data analysis, data visualization, dashboard development, and business decision support.

## 📄 License

This repository is intended for educational and portfolio purposes. 
