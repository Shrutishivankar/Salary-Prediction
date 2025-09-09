# Salary Prediction using Machine Learning

Salary Prediction is a machine learning project that predicts an individual's salary based on key factors such as years of experience and other features.  
It demonstrates how regression models can be applied to real-world datasets for predictive analytics.

---

## Features

- Data Preprocessing – Handles missing values, normalization, and splitting datasets.  
- Machine Learning Model – Implements regression algorithms for salary prediction.  
- Model Training & Evaluation – Trains the model and evaluates performance using metrics like R² Score & Mean Squared Error.  
- Prediction Interface – Allows users to input features (e.g., years of experience) and get salary predictions.  
- Interactive Visualization – Plots training data, regression line, and prediction results.  

---

## Tech Stack

- **Language:** Python  
- **Libraries:** NumPy, Pandas, Matplotlib, Scikit-learn  
- **Model:** Linear Regression / Multiple Regression  

---

## Dataset Used

- The dataset is taken from the [YBI Foundation Dataset Repository](https://github.com/YBIFoundation/Dataset/raw/main/Salary%20Data.csv).  
- It contains two columns:  
  - **YearsExperience** – Number of years of professional experience  
  - **Salary** – Annual salary in USD  

- Example dataset format:  

  | YearsExperience | Salary   |
  |-----------------|----------|
  | 1.1             | 39343.0  |
  | 2.0             | 43525.0  |
  | 3.2             | 60150.0  |
  | 4.5             | 61111.0  |
  | 5.9             | 81363.0  |

---

## Installation & Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/Salary-Prediction.git
   cd Salary-Prediction
2. **Run the script**
   ```bash
   python salary_prediction.py
