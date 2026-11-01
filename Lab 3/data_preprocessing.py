import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Sample dataset
data = {
    'Age': [20, 21, None, 23, 22],
    'Marks': [78, 85, 90, None, 88],
    'City': ['Indore', 'Bhopal', 'Indore', 'Ujjain', 'Bhopal']
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

# Encode categorical data
encoder = LabelEncoder()
df['City'] = encoder.fit_transform(df['City'])

# Scale numerical data
scaler = StandardScaler()
df[['Age', 'Marks']] = scaler.fit_transform(df[['Age', 'Marks']])

print("\nPreprocessed Data:\n", df)
