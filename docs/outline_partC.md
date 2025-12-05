## Final Project Outline – ISTA 421
**Student:** Yokutjon Tohirova  
**Project Title:** Sales Prediction & Model Comparison using Restaurant Sales Data

**1. Introduction & Problem Statement**  
- The project analyzes restaurant product-level sales data to understand what factors influence total sales and sales performance.  
- The central research question:  
**Which machine learning model (Linear Regression, Ridge, Lasso, Logistic Regression, or KNN) provides the most reliable predictions of product sales, and what features drive these predictions?**

**2. Significance**
- Accurate prediction of sales performance is essential for pricing strategy, product planning, and revenue optimization.
- Identifying the most important features can help businesses make better operational decisions.
- Comparing models demonstrates how different ML techniques behave on real business data.

**3. Dataset Description**
Source: Kaggle – Restaurant Sales Data (254 rows, ~10 columns).
Includes quantitative features (Price, Quantity Sold, Total Sales) and qualitative features (Product Name, Category).
Target variables:
- Total_Sales (regression)
- High_Sales (classification, created through feature engineering)

**4. Planned Methods & Analysis**
**A. Data Cleaning & Preprocessing**
- Handling missing values
- Converting data types
- Cleaning text fields
- Creating new variables (sales category, maybe profit, normalized features, and so on)

**B. Exploratory Data Analysis**
- Summary statistics
- Correlation heatmap
- Distribution plots (price, quantity, total sales)
- Relationship trends (Price vs Total Sales, and so on)

**C. Modeling**
- Regression Models
- Linear Regression
- Multiple Linear Regression
- Ridge Regression
- Lasso Regression

**Classification Models**
- Logistic Regression
- K-Nearest Neighbors (KNN)

**D. Feature Engineering**
- Creating High_Sales based on median threshold
- Possibly creating:
     - Price bins
     - Interaction terms
     - Standardized numerical features

**E. Model Evaluation**
- Regression Metrics
- R²
- RMSE
- MAE

**Classification Metrics**
- Accuracy
- ROC-AUC
- Confusion Matrix

**Validation Methods**
- Train/test split
- k-Fold Cross-Validation
  
**F. Model Comparison**
- Comparing all models using consistent evaluation criteria
- Identifying best performing models
- Discussing reasons (overfitting, underfitting, regularization effects, and so on)

**5. Expected Deliverables (Part D)**
- Fully cleaning dataset (in /data)
- Scripts for cleaning and modeling (in /scripts)
- Jupyter notebooks:
    - 01_EDA.ipynb
    - 02_Regression_Models.ipynb
    - 03_Classification_Models.ipynb
    - 04_Final_Model.ipynb
- Plots & metrics (in /results)
- Final written report PDF
- Updated README on GitHub

