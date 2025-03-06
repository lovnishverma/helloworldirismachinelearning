# Data Cleaning Guide

Data cleaning is a crucial step in the data preprocessing pipeline. It ensures that data is accurate, complete, and ready for analysis. This guide covers key data cleaning techniques using Python and Pandas with an example dataset.

## 📂 Example Dataset: `student_scores.csv`

Let's assume we have a dataset containing student scores with the following issues:

| Student_ID | Name   | Age | Score  | Subject  | Gender |
|------------|--------|-----|--------|----------|--------|
| 101        | Alice  | 17  | 85     | Math     | F      |
| 102        | Bob    |     | 90     | Science  | M      |
| 103        | Carol  | 18  | -1     | Math     |        |
| 104        | Dave   | 19  | 88     | Science  | M      |
| 105        | Eve    | 17  | 92     | Math     | F      |
| 106        | Frank  | 20  | 89     |          | M      |

### Issues in the Dataset:
✅ Missing values in `Age`, `Gender`, and `Subject` columns.  
✅ Invalid values (negative score).  
✅ Inconsistent formatting and duplicate records.  
✅ Outliers in the data.

---

## 🔍 Data Cleaning Steps

### 1️⃣ Load the Dataset
```python
import pandas as pd
# Load the dataset
students = pd.read_csv('student_scores.csv')
```

### 2️⃣ Handling Missing Values
#### a) Identify Missing Values
```python
print(students.isnull().sum())  # Check missing values in each column
```
#### b) Fill Missing Values
- **Fill numerical values with mean/median**
```python
students['Age'].fillna(students['Age'].median(), inplace=True)
```
- **Fill categorical values with mode**
```python
students['Gender'].fillna(students['Gender'].mode()[0], inplace=True)
students['Subject'].fillna('Unknown', inplace=True)
```

### 3️⃣ Handling Invalid Values
#### a) Removing Negative Scores
```python
students = students[students['Score'] >= 0]
```

### 4️⃣ Handling Duplicate Records
```python
students.drop_duplicates(inplace=True)
```

### 5️⃣ Standardizing Text Data
```python
students['Name'] = students['Name'].str.title()
students['Subject'] = students['Subject'].str.capitalize()
```

### 6️⃣ Handling Outliers
```python
import numpy as np
Q1 = students['Score'].quantile(0.25)
Q3 = students['Score'].quantile(0.75)
IQR = Q3 - Q1
students = students[(students['Score'] >= Q1 - 1.5 * IQR) & (students['Score'] <= Q3 + 1.5 * IQR)]
```

### 7️⃣ Convert Data Types
```python
students['Student_ID'] = students['Student_ID'].astype(str)
students['Age'] = students['Age'].astype(int)
```

---

## ✅ Cleaned Dataset
After applying these steps, the dataset will be cleaned, making it ready for analysis or machine learning models.

---

## 🚀 Summary
- **Handled missing values** (filled numerical with median and categorical with mode)
- **Removed invalid and duplicate data**
- **Standardized text formatting**
- **Detected and removed outliers**
- **Converted data types correctly**

With this guide, you can effectively clean datasets before performing analysis or building machine learning models. 
