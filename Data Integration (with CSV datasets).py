import pandas as pd

# Load two datasets
df_emp = pd.read_csv("sample_dataset.csv")       # Employee details
df_dept = pd.read_csv("department_dataset.csv")  # Department info

# --- Data Integration ---
df_integrated = pd.merge(df_emp, df_dept, on="EmpID", how="left")
print("Integrated Data:\n", df_integrated)