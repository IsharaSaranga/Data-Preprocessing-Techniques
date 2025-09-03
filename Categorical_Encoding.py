import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Load dataset
data = pd.read_csv("../department_dataset.csv")

print("Original Data:\n", data.head())

# Label Encoding (for one column)
le = LabelEncoder()
data['Department_LabelEncoded'] = le.fit_transform(data['Department'])
print("\nAfter Label Encoding:\n", data.head())

# One-Hot Encoding
data_onehot = pd.get_dummies(data, columns=['Department'])
print("\nAfter One-Hot Encoding:\n", data_onehot.head())
