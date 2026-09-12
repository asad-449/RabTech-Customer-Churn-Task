# Customer Churn Prediction

## RabTech Academy AI & ML Internship Task

This project was completed as part of the RabTech Academy Artificial Intelligence & Machine Learning Internship Program.

### Project Objective

The objective of this project is to predict whether a customer is likely to churn (leave the service) based on customer behavior and usage patterns while demonstrating Machine Learning, Deep Learning, Model Evaluation, and Deployment concepts.

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
* Deep Learning Sentiment Analysis
* FastAPI Deployment

### Prediction Target

**churned**

* 1 = Customer Churned
* 0 = Customer Retained

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

---

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

---

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

---

## Task 5 - Deep Learning Sentiment Analysis

Implemented:

* TF-IDF Vectorization
* Multi-Layer Neural Network
* Batch Normalization
* Dropout Regularization
* Early Stopping
* Training and Validation
* Accuracy and Loss Curves
* Sample Inference Predictions

Notebook:

* Deep_Learning_Sentiment_Analysis.ipynb

---

## Task 6 - FastAPI Deployment

Implemented:

* FastAPI REST API
* /predict Endpoint
* Docker Containerization
* Unit Testing
* API Documentation

Files:

* app.py
* Dockerfile
* requirements.txt
* test_api.py

---

### Repository Structure

```text id="r9k8zv"
README.md
ML_Problem_Framing_Memo.md
Responsible_Data_Card.md
Risk_Register.md
Baseline_Model.py
customer-churn-training.csv
Model_Comparison.ipynb
best_model.joblib
Deep_Learning_Sentiment_Analysis.ipynb
app.py
Dockerfile
requirements.txt
test_api.py
```

### Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* TensorFlow / Keras
* FastAPI
* Joblib
* Docker
* Google Colab
* Jupyter Notebook

### Author

Asad Alam

B.Tech CSE, IILM University
