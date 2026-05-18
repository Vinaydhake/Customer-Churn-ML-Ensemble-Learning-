# Customer-Churn-ML-Ensemble-Learning-
# 202401110031 Vinay Sandip Dhake
# 202401110036 Kishor Kaple
# 202401110043 Sudarshan Bansude

# mmep_12.12_26 is Customer Churn Analysis using Machine Learning Reasearch Paper

# ALL other files included in ZIP file
# Customer Churn Prediction using Machine Learning

## Project Overview

This project predicts whether a telecom customer is likely to leave the company (Customer Churn) using Machine Learning techniques. The objective is to compare multiple classification and ensemble learning algorithms and identify the best-performing model.

Customer churn prediction helps telecom companies identify customers at risk of leaving so they can take preventive actions and improve retention.

---

## Problem Statement

Customer churn is a major challenge in the telecom industry because losing existing customers affects revenue and acquiring new customers is more expensive.

The goal of this project is:

* Predict customer churn
* Compare ML models
* Evaluate ensemble learning techniques
* Identify important factors influencing churn

---

## Dataset

Dataset Used:
**Telco Customer Churn Dataset**

Features include:

* Gender
* Tenure
* Monthly Charges
* Contract Type
* Internet Service
* Payment Method
* Total Charges
* Senior Citizen
* Churn (Target)

Target Variable:

* Churn = Yes/No

---

## Technologies Used

* Python
* Google Colab
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## Methodology

### Step 1: Data Loading

Dataset loaded using pandas.

### Step 2: Data Cleaning

* Converted TotalCharges into numerical values
* Handled missing values
* Removed unnecessary columns like customerID

### Step 3: Data Preprocessing

* One Hot Encoding for categorical variables
* Feature scaling using StandardScaler

### Step 4: Train-Test Split

Dataset divided:

* Training Data: 80%
* Testing Data: 20%

### Step 5: Model Building

Classification Models:

* Logistic Regression
* Decision Tree
* K-Nearest Neighbors (KNN)

Ensemble Models:

* Random Forest
* AdaBoost

### Step 6: Model Evaluation

Metrics used:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## Results

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 82.04%   |
| AdaBoost            | 81.26%   |
| Random Forest       | 79.28%   |
| KNN                 | 77.43%   |
| Decision Tree       | 72.46%   |

Logistic Regression achieved the highest accuracy.

---

## Feature Importance

Important factors affecting churn:

* Tenure
* Monthly Charges

Insights:

* Customers with lower tenure are more likely to churn.
* Higher monthly charges may increase churn probability.

---

## Conclusion

Multiple machine learning models were implemented and compared.

Logistic Regression performed best on this dataset with 82.04% accuracy.

Although ensemble methods generally improve performance, Logistic Regression slightly outperformed Random Forest and AdaBoost, indicating relatively linear patterns in the dataset.

---

## Future Scope

* Hyperparameter tuning
* XGBoost implementation
* Real-time prediction system
* Deployment using Streamlit or Flask
* Explainable AI using SHAP

---

## Author

Machine Learning Mini Project
Customer Churn Prediction using Classification and Ensemble Learning
Vinay
