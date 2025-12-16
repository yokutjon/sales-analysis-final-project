# Restaurant Sales Analysis and High Sales Prediction
Project Overview

This project analyzes restaurant sales transactions to identify factors associated with high-value sales and to evaluate machine learning models for predicting sales performance. The goal is to predict whether a transaction results in high sales based on transaction-level features such as price, quantity sold, purchase type, and city.
The project demonstrates a complete machine learning workflow including data preprocessing, exploratory data analysis, feature engineering, model selection, evaluation, and interpretation.

Dataset
The dataset contains 254 restaurant transactions, where each observation represents a single sales transaction. Key variables include:
- Price
- Quantity sold
- Purchase type
- City
- Payment method
- Manager
A new feature, total_sales, was engineered as the product of price and quantity.
The target variable, high_sales, is a binary indicator representing whether a transaction’s total sales exceed the median value.

Methodology
The analysis follows these steps:
1. Data cleaning and preprocessing
2. Exploratory data analysis with visualizations
3. Feature engineering
4. Definition of a binary classification task
5. Train test split with stratification
6. Model training and evaluation
The following models were evaluated:
- Logistic Regression (baseline)
- Ridge Logistic Regression
- Lasso Logistic Regression
- Decision Tree Classifier
Model performance was compared using classification accuracy, with additional interpretation of model complexity and stability.

Key Findings
- Price, quantity sold, purchase type, and city are meaningful predictors of high sales transactions.
- Logistic regression provides a strong and interpretable baseline model.
- Regularized logistic regression models improve stability and help control model complexity.
- Decision trees capture nonlinear relationships but may overfit on small datasets.
Overall, regularized logistic regression offers the best balance between interpretability and predictive performance for this dataset.

Repository Structure
├── data/
│   └── Sales-Data-Analysis.csv
│
├── notebooks/
│   └── 01_EDA.ipynb
│
├── scripts/
│   └── clean_data.py
│
├── results/
│   ├── plots/
│   ├── metrics/
│   └── tables/
│
└── README.md

How to Run
1. Clone the repository
2. Open 01_EDA.ipynb in Jupyter
3. Run all cells from top to bottom
All preprocessing and modeling steps are fully reproducible.

Tools and Libraries
- Python
- pandas
- numpy
- scikit-learn
- matplotlib

 Author
 Yokutjon Tohirova
 ISTA 421 – Final Project



