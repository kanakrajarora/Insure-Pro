
# InsurePro: Insurance Premium Prediction System

## Overview
InsurePro is an end-to-end machine learning system designed to predict medical insurance premiums using ensemble learning techniques. The system combines multiple regression models through stacking and provides real-time predictions via a Streamlit-based web application. It also includes PDF report generation for practical business use.

---

## Features
- Ensemble learning using Stacking Regressor
- Models used: Random Forest, Gradient Boosting, XGBoost, Ridge (meta-learner)
- Advanced feature engineering (BMI categories, age groups, interaction features)
- Cross-validation and hyperparameter tuning
- Streamlit-based interactive web application
- Real-time premium prediction
- PDF quote generation
- Business-oriented risk assessment

---

## Dataset
- Source: Medical Insurance Dataset (Kaggle) https://www.kaggle.com/datasets/mosapabdelghany/medical-insurance-cost-dataset
- Records: 2772
- Features:
  - Age
  - Sex
  - BMI
  - Number of Children
  - Smoker Status
  - Region
- Target:
  - Insurance Charges

---

## Project Structure
```

├── app.py                  # Streamlit application
├── stacking_model.pkl      # Trained ML model
├── model_columns.pkl       # Feature columns
├── Medical_insurance.csv   # Dataset
├── code copy.ipynb          # Model development
├── README.md               # Project documentation

```

---

## Methodology

### 1. Data Preprocessing
- Removed duplicates
- Verified no missing values
- Performed exploratory data analysis

### 2. Feature Engineering
- BMI categories: underweight, normal, overweight, obese
- Age groups: teen, young adult, adult, senior
- Interaction feature: smoker × BMI
- One-hot encoding for categorical variables

### 3. Model Development
- Linear Regression, Ridge, Lasso
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

### 4. Ensemble Learning
- Stacking Regressor with:
  - Base models: RF, GB, XGB
  - Meta-learner: Ridge Regression

### 5. Evaluation Metrics
- R² Score
- RMSE
- MAE
- Cross-validation (5-fold)

---

## Results

| Model                    | R²    | RMSE   | MAE    |
|--------------------------|------|--------|--------|
| Linear Regression        | 0.889 | 4524.85 | 2784.31 |
| Decision Tree            | 0.891 | 4471.10 | 2684.19 |
| Gradient Boosting        | 0.901 | 4273.12 | 2463.78 |
| Random Forest (Tuned)    | 0.901 | 4261.83 | 2431.13 |
| XGBoost (Tuned)          | 0.894 | 4410.71 | 2643.23 |
| Stacking (Final Model)   | 0.905 | 4183.14 | 2419.77 |

---

## Web Application

The Streamlit application allows users to:
- Input customer details (age, height, weight, etc.)
- Automatically compute BMI
- Predict insurance premium
- View risk category
- Download PDF insurance quote

---

## Installation

### 1. Clone Repository
```
git clone [https://github.com/kanakrajarora/InsurePro.git](https://github.com/kanakrajarora/InsurePro.git)
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Run Application
```
streamlit run app.py
```

---

## Usage
1. Enter customer details in the sidebar
2. Click "Predict Premium"
3. View predicted insurance charges
4. Download PDF quote if required

---

## Limitations
- Dataset is relatively small (2772 records)
- Limited features (no medical history or lifestyle data)
- Slight heteroscedasticity observed in high-cost predictions

---

## Future Work
- Integration of SHAP for explainability
- Inclusion of additional health-related features
- Deployment on cloud platforms
- API development for enterprise integration
- Fairness and bias analysis

---

## Technologies Used
- Python
- Scikit-learn
- XGBoost
- Pandas, NumPy
- Matplotlib, Seaborn
- Streamlit
- ReportLab

---

## Author
Kanak Raj Arora

---

## License
This project is for academic and research purposes.
