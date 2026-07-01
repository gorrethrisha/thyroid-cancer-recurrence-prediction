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

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

## Methodology

The following steps were followed during the development of the project:

1. Data Overview
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature and Target Separation
5. Train-Test Split
6. Feature Scaling
7. Model Training and Evaluation
   - Logistic Regression
   - Support Vector Classifier (SVC)
   - Decision Tree Classifier
   - Random Forest Classifier
8. Model Comparison
9. Final Model Selection

## Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 84.93% | 78.95% | 68.18% | 73.17% |
| Support Vector Classifier (SVC) | 90.41% | 85.71% | 81.82% | 83.72% |
| Decision Tree Classifier | 91.78% | 80.77% | 95.45% | 87.50% |
| Random Forest Classifier | 95.89% | 91.30% | 95.45% | 93.33% |

## Final Model Selection

Logistic Regression, Support Vector Classifier (SVC), Decision Tree, and Random Forest Classifier models were trained and evaluated for thyroid cancer recurrence prediction. Although Logistic Regression and SVC achieved strong performance, Decision Tree and Random Forest demonstrated superior ability in identifying recurrence cases.

Among all the models, the Random Forest classifier achieved the highest accuracy, precision, and F1-score while maintaining an excellent recall value. The model correctly identified almost all recurrence cases and produced very few false predictions.

Since correctly predicting thyroid cancer recurrence is important in medical applications, **the Random Forest classifier was selected as the final model for Thyroid Cancer Recurrence Detection.**

## Streamlit Web Application

A Streamlit-based web application was developed to provide an interactive interface for Thyroid Cancer Recurrence Prediction.

The application allows users to enter patient clinical and pathological information and instantly predicts whether thyroid cancer recurrence is likely to occur using the trained machine learning model.

## Project Files

- `Thyroid Cancer Recurrence Prediction.ipynb` - Complete notebook containing data preprocessing, model training, and evaluation.
- `app.py` - Streamlit web application for thyroid cancer recurrence prediction.
- `thyroid_recurrence_model.pkl` - Saved trained Random Forest model.
- `requirements.txt` - Required Python packages for running the application and reproducing the project environment.
- `README.md` - Project documentation.

## Conclusion

A Thyroid Cancer Recurrence Detection system was successfully developed and multiple machine learning algorithms were trained and evaluated for prediction performance. The developed system can assist in identifying recurrence cases and support healthcare decision-making processes.
