# 🏠 House Price Prediction Using Machine Learning

## 📌 Project Overview

This project focuses on predicting house prices using **Machine Learning and Linear Regression**.
The model uses different property features, such as area, bedrooms, bathrooms, stories, and other facilities, to predict the price of a house.

The project includes data preprocessing, categorical feature encoding, feature scaling, model training, and model evaluation.
A **Streamlit web application** allows users to enter house details and obtain a predicted price.

## 🎯 Project Objectives

- Analyze housing data using Python.
- Perform data preprocessing and handle categorical features.
- Encode categorical variables using numerical values such as 0 and 1.
- Split the dataset into training and testing sets.
- Scale features using StandardScaler.
- Build a Linear Regression model.
- Evaluate model performance using Mean Squared Error (MSE) and R² Score.
- Develop an interactive application to predict house prices.

## 🛠️ Technologies and Libraries Used

The following Python libraries were used in this project:

| Library | Purpose |
|---|---|
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations and array handling |
| Matplotlib | Data visualization |
| Seaborn | Statistical data visualization |
| Scikit-learn | Machine Learning model development and evaluation |
| Streamlit | Creating the interactive web application |
| Joblib | Saving and loading the trained model and scaler |

### Scikit-learn Modules

- `train_test_split` — Splits the dataset into training and testing sets.
- `StandardScaler` — Standardizes numerical features.
- `LinearRegression` — Builds the Linear Regression model.
- `mean_squared_error` — Calculates Mean Squared Error.
- `r2_score` — Calculates the R² Score.
- `mean_absolute_error` — Calculates Mean Absolute Error.

## 📂 Project Workflow

### 1. Data Loading and Exploration
- Loaded the housing dataset using Pandas.
- Explored the dataset to understand its structure and features.
- Identified numerical and categorical columns.

### 2. Data Preprocessing
- Prepared the dataset for Machine Learning.
- Processed categorical columns into numerical representations.
- Encoded binary categorical values using 0 and 1.

### 3. Feature Selection
Selected the relevant input features required to predict house prices.

Examples of property features include:
- Area in square feet
- Number of bedrooms
- Number of bathrooms
- Number of stories
- Main road access
- Guestroom availability
- Basement availability
- Hot water heating facility
- Air conditioning
- Parking availability
- Preferred area
- Furnishing status

### 4. Train-Test Split
Used `train_test_split` from Scikit-learn to divide the dataset into training and testing sets.

This allows the model to be trained on one portion of the data and evaluated on separate, unseen data.

### 5. Feature Scaling
Applied `StandardScaler` to standardize the input features before making predictions.

The fitted scaler was saved and reused when processing user inputs in the Streamlit application.

### 6. Model Building
Implemented **Linear Regression**, a supervised Machine Learning algorithm used to predict continuous numerical values.

The model learns relationships between property features and house prices from the training data.

### 7. Model Evaluation
Evaluated model performance using the following metrics:

**Mean Squared Error (MSE)**

MSE measures the average squared difference between actual and predicted house prices. A lower MSE generally indicates smaller prediction errors.

**R² Score (Coefficient of Determination)**

R² measures how well the model explains the variation in the target variable. A score closer to 1 generally indicates a better fit on the evaluated dataset.

### 8. House Price Prediction
Saved the trained model and scaler using Joblib.

Created an interactive Streamlit application where users can enter property details and receive a predicted house price.

## 📊 Model Evaluation Metrics

The following metrics were used to evaluate the Linear Regression model:

- Mean Squared Error (MSE)
- R² Score


## 🚀 How to Run the Project

### Prerequisites

Install Python on your system.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### Step 2: Navigate to the Project Folder

```bash
cd House-Price-Prediction-ML
```

### Step 3: Install the Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
```

### Step 4: Run the Streamlit Application

```bash
streamlit run Python_projectfile.py
```

The application will open in your web browser.

### Step 5: Predict House Prices

1. Enter the house area in square feet.
2. Enter the number of bedrooms and bathrooms.
3. Enter the other property details.
4. Click the **Predict Price** button.
5. View the predicted house price.

## 📁 Project Files

| File | Description |
|---|---|
| `Python_projectfile.py` | Streamlit application for house price prediction |
| `ML.py` | Additional Python project code; verify its exact role |
| `house_model.pkl` | Saved trained Machine Learning model |
| `scale.pkl` | Saved feature scaler |

## 💡 Key Learnings

Through this project, I gained practical experience in:

- Data preprocessing and exploratory data analysis.
- Working with numerical and categorical data.
- Encoding categorical variables.
- Feature scaling using StandardScaler.
- Training a Linear Regression model.
- Evaluating model performance using MSE and R² Score.
- Saving and loading Machine Learning models.
- Developing an interactive application using Streamlit.



## 👩‍💻 Author

**Sapna Gupta**

Aspiring Data Analyst | Data Science with AI & ML Student

Interested in Python, SQL, Data Analytics, and Machine Learning.

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback!
