
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("HR Analytics Project Started")

# Load dataset
df = pd.read_csv("Dataset/HR_Analytics_Cleaned.xlsx.csv")

# Display first 5 records
print("\nFirst 5 Records:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())


# Employee Attrition Analysis

print("\nEmployee Attrition Count:")
print(df["Attrition"].value_counts())

# Calculate attrition rate
total_employees = len(df)
employees_left = (df["Attrition"] == "Yes").sum()

attrition_rate = (employees_left / total_employees) * 100

print("\nTotal Employees:", total_employees)
print("Employees Left:", employees_left)
print("Attrition Rate:", round(attrition_rate, 2), "%")


# Department-wise Attrition Analysis

print("\nDepartment-wise Employee Count:")

department_count = df.groupby("Department").size()

print(department_count)

print("\nDepartment-wise Attrition Count:")

department_attrition = df[df["Attrition"] == "Yes"].groupby("Department").size()

print(department_attrition)

print("\nDepartment-wise Attrition Rate:")

department_rate = (
    df[df["Attrition"] == "Yes"].groupby("Department").size()
    / df.groupby("Department").size()
) * 100

print(department_rate.round(2))


import matplotlib.pyplot as plt

# Department-wise Attrition Chart

department_rate = (
    df[df["Attrition"] == "Yes"].groupby("Department").size()
    / df.groupby("Department").size()
) * 100

plt.figure(figsize=(8, 5))

department_rate.plot(kind="bar")

plt.title("Department-wise Employee Attrition Rate")
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")

plt.xticks(rotation=0)
plt.tight_layout()

plt.show()


import matplotlib.pyplot as plt

# 1. Gender-wise Employee Count
print("\nGender-wise Employee Count:")
print(df.groupby("Gender").size())

# 2. Gender-wise Attrition Count
print("\nGender-wise Attrition Count:")
gender_attrition = df[df["Attrition"] == "Yes"].groupby("Gender").size()
print(gender_attrition)

# 3. Gender-wise Attrition Rate
print("\nGender-wise Attrition Rate:")

gender_rate = (
    df[df["Attrition"] == "Yes"].groupby("Gender").size()
    / df.groupby("Gender").size()
) * 100

print(gender_rate.round(2))

# 4. Gender-wise Attrition Chart
plt.figure(figsize=(7, 5))
gender_rate.plot(kind="bar")

plt.title("Gender-wise Employee Attrition Rate")
plt.xlabel("Gender")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Age-wise Employee Attrition Analysis

# Create age groups
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 65],
    labels=["18-25", "26-35", "36-45", "46-55", "56-65"]
)

# Total employees in each age group
print("\nAge Group-wise Employee Count:")
print(df.groupby("Age_Group").size())

# Employees who left in each age group
print("\nAge Group-wise Attrition Count:")
age_attrition = df[df["Attrition"] == "Yes"].groupby("Age_Group").size()
print(age_attrition)

# Attrition rate
print("\nAge Group-wise Attrition Rate:")

age_rate = (
    age_attrition / df.groupby("Age_Group").size()
) * 100

print(age_rate.round(2))

import matplotlib.pyplot as plt

# Age-wise Employee Attrition Chart

plt.figure(figsize=(8, 5))

age_rate.plot(kind="bar")

plt.title("Age Group-wise Employee Attrition Rate")
plt.xlabel("Age Group")
plt.ylabel("Attrition Rate (%)")

plt.xticks(rotation=0)
plt.tight_layout()

plt.show()

# Overtime vs Employee Attrition Analysis

print("\nOvertime-wise Employee Count:")
print(df.groupby("OverTime").size())

print("\nOvertime-wise Attrition Count:")
overtime_attrition = (
    df[df["Attrition"] == "Yes"].groupby("OverTime").size()
)
print(overtime_attrition)

print("\nOvertime-wise Attrition Rate:")

overtime_rate = (
    overtime_attrition / df.groupby("OverTime").size()
) * 100

print(overtime_rate.round(2))

# Overtime Attrition Chart

import matplotlib.pyplot as plt

plt.figure(figsize=(7, 5))

overtime_rate.plot(kind="bar")

plt.title("Overtime vs Employee Attrition Rate")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Job Role-wise Employee Attrition Analysis

print("\nJob Role-wise Employee Count:")
print(df.groupby("JobRole").size())

print("\nJob Role-wise Attrition Count:")

job_attrition = (
    df[df["Attrition"] == "Yes"].groupby("JobRole").size()
)

print(job_attrition)

print("\nJob Role-wise Attrition Rate:")

job_rate = (
    job_attrition / df.groupby("JobRole").size()
) * 100

print(job_rate.round(2))

# Job Role-wise Attrition Chart

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

job_rate.sort_values().plot(kind="bar")

plt.title("Job Role-wise Employee Attrition Rate")
plt.xlabel("Job Role")
plt.ylabel("Attrition Rate (%)")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Job Satisfaction vs Employee Attrition Analysis

print("\nJob Satisfaction-wise Employee Count:")
print(df.groupby("JobSatisfaction").size())

print("\nJob Satisfaction-wise Attrition Count:")

satisfaction_attrition = (
    df[df["Attrition"] == "Yes"]
    .groupby("JobSatisfaction").size()
)

print(satisfaction_attrition)

print("\nJob Satisfaction-wise Attrition Rate:")

satisfaction_rate = (
    satisfaction_attrition / df.groupby("JobSatisfaction").size()
) * 100

print(satisfaction_rate.round(2))

# Job Satisfaction Attrition Chart

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

satisfaction_rate.plot(kind="bar")

plt.title("Job Satisfaction vs Employee Attrition")
plt.xlabel("Job Satisfaction Level")
plt.ylabel("Attrition Rate (%)")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Monthly Income vs Employee Attrition Analysis

# Create income groups
df["Income_Group"] = pd.cut(
    df["MonthlyIncome"],
    bins=[0, 5000, 10000, 15000, 20000],
    labels=["0-5000", "5001-10000", "10001-15000", "15001-20000"]
)

# Total employees in each income group
print("\nIncome Group-wise Employee Count:")
print(df.groupby("Income_Group").size())

# Employees who left
print("\nIncome Group-wise Attrition Count:")

income_attrition = (
    df[df["Attrition"] == "Yes"]
    .groupby("Income_Group").size()
)

print(income_attrition)

# Attrition rate
print("\nIncome Group-wise Attrition Rate:")

income_rate = (
    income_attrition / df.groupby("Income_Group").size()
) * 100

print(income_rate.round(2))

# Create chart
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))

income_rate.plot(kind="bar")

plt.title("Monthly Income vs Employee Attrition Rate")
plt.xlabel("Monthly Income Group")
plt.ylabel("Attrition Rate (%)")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Export Processed HR Dataset

df.to_csv(
    "Dataset/HR_Analytics_Processed.csv",
    index=False
)

print("\nProcessed HR dataset exported successfully!")


