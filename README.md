# E-commerce Conversion Funnel Analysis

An end-to-end **Data Analytics & Data Science** project focused on understanding customer conversion behaviour, identifying funnel drop-offs, analysing revenue efficiency, and predicting purchase likelihood.

## Problem Statement

E-commerce platforms generate large amounts of session-level data, but raw data does not directly show where potential customers are being lost or where revenue opportunities are being missed.

This project analyses the customer journey:

**Website Visit → Product View → Add to Cart → Checkout → Purchase**

The goal is to identify conversion drop-offs, revenue leakage, channel and campaign performance, customer behaviour, and purchase patterns.

## Objectives

- Analyse the complete e-commerce conversion funnel
- Identify major customer drop-off stages
- Compare channels, campaigns, devices and user types
- Analyse order value, realised revenue and revenue leakage
- Track conversion and purchase trends over time
- Build a machine learning model for purchase prediction
- Create Power BI dashboards for business analysis
- Build a Streamlit application for purchase prediction

## Workflow

**Raw Data → Python Cleaning → SQL Analysis → Power BI → Machine Learning → Streamlit Application**

## Dataset

- **Records:** 120,000 sessions
- **Columns:** 17
- **Period:** July 2025 – December 2025
- **Granularity:** Session-level e-commerce data

Key columns:

`user_id`, `session_id`, `date`, `month`, `channel`, `campaign_type`, `device`, `user_type`, `region`, `visited_website`, `viewed_product`, `added_to_cart`, `checkout_started`, `purchase_completed`, `discount_applied`, `order_value`, `revenue`

## Technologies

Python • Pandas • NumPy • MySQL • SQL • Power BI • DAX • Scikit-learn • Random Forest • XGBoost • Streamlit • Joblib • GitHub

## SQL Analysis

SQL was used to analyse funnel conversion, drop-offs, channel and campaign performance, customer behaviour, discount impact, revenue leakage, monthly trends and revenue efficiency.

[SQL Analysis Report](report/Ecommerce_Funnel_SQL_Analysis_Report.pdf)  
[SQL Queries](sql/funnel_analysis.sql)

## Power BI Dashboards

### Page 1 — Executive Overview

Overall funnel, conversion trends, revenue efficiency and segment performance.

[Dashboard Page 1](dashboard/Page_1_Executive_Overview.png)

### Page 2 — Conversion & Revenue Optimization

Funnel drop-offs, revenue leakage, discount impact, campaign performance and purchase trends.

[Dashboard Page 2](dashboard/Page_2_Conversion_Revenue_Optimization.png)

[Power BI File](dashboard/E-commerce_Conversion_Funnel_Analysis.pbix)

## Machine Learning

A classification model was developed to predict whether a customer session is likely to result in a purchase.

Models tested:

- Logistic Regression
- Random Forest
- XGBoost

The final Streamlit application uses a **Random Forest Classifier** with a **92% decision threshold**.

## Streamlit Application

The application accepts customer/session characteristics and returns:

- Purchase prediction
- Purchase probability
- Decision threshold
- Model information
- Business interpretation

**Live Streamlit App:** To be added after deployment.

## Project Report

[Full Project Report](report/Ecommerce_Conversion_Funnel_Analysis_Project_Report.pdf)

## Repository Structure

```text
├── app/
│   └── app.py
├── dashboard/
│   ├── E-commerce_Conversion_Funnel_Analysis.pbix
│   ├── Page_1_Executive_Overview.png
│   └── Page_2_Conversion_Revenue_Optimization.png
├── data/
│   └── cleaned_data.csv
├── models/
│   └── rf_purchase_model.pkl
├── notebooks/
│   ├── data_clean.ipynb
│   ├── data_to_sql.ipynb
│   └── ml_model.ipynb
├── report/
│   ├── Ecommerce_Conversion_Funnel_Analysis_Project_Report.pdf
│   └── Ecommerce_Funnel_SQL_Analysis_Report.pdf
├── sql/
│   └── funnel_analysis.sql
├── .gitignore
└── README.md
```

## Author

**Akash Chauhan**  
Data Analytics & Data Science

GitHub: https://github.com/AKASH-aAI
