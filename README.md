# Thyroid Cancer Recurrence Detection

## Project Overview

This project develops a machine learning-based Thyroid Cancer Recurrence Prediction system to determine whether a patient experiences thyroid cancer recurrence after treatment using various clinical and pathological features.

## Objective

The primary objective of this project is to develop a machine learning model that can detect thyroid cancer recurrence outcomes while identifying the most effective classification algorithm for the problem.

## Dataset Information

* Total Records: **383**
* Records after removing duplicates: **364**
* Total Features: **17**
* Target Variable: **Recurred**

  * `0` → No Recurrence
  * `1` → Cancer Recurred

### Features Used for Training

* Age
* Gender
* Smoking
* Hx Smoking
* Hx Radiotherapy
* Thyroid Function
* Physical Examination
* Adenopathy
* Pathology
* Focality
* Risk
* T (Tumor classification)
* N (Nodal classification)
* M (Metastasis classification)
* Stage
* Response

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

## Methodology

The following steps were followed during the development of the project:

1. Data Overview
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature and Target Separation
5. Train-Test Split
6. Feature Scaling
7. Model Training and Evaluation6. Model Training and Evaluation
   - Logistic Regression
   - Support Vector Classifier (SVC)
   - Decision Tree Classifier
   - Random Forest Classifier
8. Model Comparison
9. Final Model Selection

## Model Performance

| Model                           | Accuracy | Precision | Recall   | F1 Score |
| ------------------------------- | -------- | --------- | -------- | -------- |
| Logistic Regression             | 0.849315 | 0.789474  | 0.681818 | 0.731707 |
| Support Vector Classifier (SVC) | 0.904110 | 0.857143  | 0.818182 | 0.837209 |
| Decision Tree Classifier        | 0.917808 | 0.807692  | 0.954545 | 0.875000 |
| Random Forest Classifier        | 0.958904 | 0.913043  | 0.954545 | 0.933333 |

## Final Model Selection

Logistic Regression, Support Vector Classifier (SVC), Decision Tree, and Random Forest Classifier models were trained and evaluated for thyroid cancer recurrence prediction. Although Logistic Regression and SVC achieved strong performance, Decision Tree and Random Forest demonstrated superior ability in identifying recurrence cases.

Among all the models, the Random Forest classifier achieved the highest accuracy, precision, and F1-score while maintaining an excellent recall value. The model correctly identified almost all recurrence cases and produced very few false predictions.

Since correctly predicting thyroid cancer recurrence is important in medical applications, **the Random Forest classifier was selected as the final model for Thyroid Cancer Recurrence Detection.**

## Conclusion

A Thyroid Cancer Recurrence Detection system was successfully developed and multiple machine learning algorithms were trained and evaluated for prediction performance. The developed system can assist in identifying recurrence cases and support healthcare decision-making processes.
