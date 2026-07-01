# Student Performance Prediction System 

## Project Overview

This project is developed using Python and Pandas to handle and analyze student performance data.

The system performs data loading, cleaning, transformation, analysis, and report generation from a CSV dataset.

---

## Technologies Used

- Python
- Pandas
- CSV Data Processing

---

## Project Structure

Student_Data_Project/
│
├── data/
│ └── student_dataset_v2.csv
│
├── output/
│ ├── cleaned_data.csv
│ ├── toppers.csv
│ ├── failed_students.csv
│ └── report.csv
│
├── src/
│ ├── load_data.py
│ ├── clean_data.py
│ ├── transform.py
│ ├── analyze.py
│ └── report.py
│
├── main.py
│
└── README.md

---

## Modules Description

### Data Loading (`load_data.py`)
- Reads CSV dataset using Pandas.
- Displays records, columns, shape, and data types.

### Data Cleaning (`clean_data.py`)
- Handles missing values.
- Removes duplicate records.
- Validates marks, attendance, and study hours.
- Saves cleaned dataset.

### Data Transformation (`transform.py`)
Creates new columns:
- Grade
- Result
- Performance Score

### Data Analysis (`analyze.py`)
Performs:
- Average, highest, and lowest marks.
- Attendance and study hour analysis.
- Pass/fail percentage.
- Grade distribution.
- Statistical analysis and correlation.

### Report Generation (`report.py`)
Generates:
- Student performance report.
- Top performers list.
- Failed students list.

---

## How to Run

Install required library:
pip install pandas

---

---

## Output Files

Generated files are stored inside the output folder:

- `cleaned_data.csv` - Cleaned student dataset
- `toppers.csv` - Top-performing students
- `failed_students.csv` - Failed students
- `report.csv` - Final performance report

---

## Learning Outcomes

- Data handling using Pandas.
- Data cleaning and preprocessing.
- Data transformation and analysis.
- CSV file handling.
- Modular Python programming.

---




# 🎓 Student Marks Prediction App

A simple Machine Learning web application built with **Streamlit** that predicts a student's marks based on their **study hours** and **attendance percentage**.

## Features

* Predicts marks using a trained **Linear Regression** model.
* Interactive and user-friendly Streamlit interface.
* Fast predictions with a pre-trained `.pkl` model.
* No separate frontend or backend required.

## Tech Stack

* Python
* Streamlit
* Scikit-learn
* NumPy
* Joblib

## Project Structure

```text
MarksPrediction/
│── app.py
│── marks_prediction_model.pkl
│── requirements.txt
│── README.md
```

## Installation

1. Clone the repository.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## How It Works

1. Enter the student's study hours.
2. Select the attendance percentage.
3. Click **Predict Marks**.
4. The application uses the trained Linear Regression model to estimate the student's marks.







