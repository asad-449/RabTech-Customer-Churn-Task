# Customer Churn Prediction

## RabTech Academy AI & ML Internship Task

This project was completed as part of the RabTech Academy Artificial Intelligence & Machine Learning Internship Program.

### Project Objective

The objective of this project is to predict whether a customer is likely to churn (leave the service) based on customer behavior and usage patterns.

### Dataset

The project uses the provided customer churn training dataset containing customer information such as:

* Tenure Months
* Support Tickets
* Monthly Spend
* Last Login Days
* Plan Type
* Churn Status

### Project Deliverables

* ML Problem Framing Memo
* Responsible Data Card
* Baseline Model
* Risk Register
* Machine Learning Preprocessing Pipeline
* Model Training and Comparison

### Prediction Target

**churned**

* 1 = Customer Churned
* 0 = Customer Retained

### Baseline Approach

A simple rule-based baseline is used before applying machine learning models.

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

## Task 3 - Machine Learning Preprocessing Pipeline

Implemented:

* Train/Test Split before transformations
* Missing Value Imputation
* Feature Scaling
* One-Hot Encoding
* ColumnTransformer
* Scikit-Learn Pipeline
* Correlation Analysis
* Feature Importance Analysis

## Task 4 - Model Training and Comparison

Models Implemented:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* Gradient Boosting Classifier

Hyperparameter Optimization:

* GridSearchCV
* 5-Fold Cross Validation

Model Evaluation:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Analysis
* Confusion Matrix

Artifacts Generated:

* Model_Comparison.ipynb
* best_model.joblib

### Repository Structure

```text
README.md
ML_Problem_Framing_Memo.md
Responsible_Data_Card.md
Risk_Register.md
Baseline_Model.py
customer-churn-training.csv
Model_Comparison.ipynb
best
```
