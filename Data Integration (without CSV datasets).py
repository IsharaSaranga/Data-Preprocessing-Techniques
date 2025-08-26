import pandas as pd

# Employee dataset
emp_data = {
    "EmpID": [1, 2, 3, 4, 5],
    "Age": [25, 32, 47, 51, 62],
    "Salary": [35000, 48000, 56000, 60000, 72000]
}
df_emp = pd.DataFrame(emp_data)

# Department dataset
dept_data = {
    "EmpID": [1, 2, 3, 4, 5],
    "Department": ["IT", "HR", "Finance", "Marketing", "Operations"]
}
df_dept = pd.DataFrame(dept_data)

# --- Data Integration ---
df_integrated = pd.merge(df_emp, df_dept, on="EmpID", how="left")
print("Integrated Data:\n", df_integrated)
