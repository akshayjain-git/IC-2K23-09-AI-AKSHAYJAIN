import pandas as pd

# Sample dataset
data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Age': [20, 21, 22, 23, 24],
    'Marks': [75, 82, 91, 68, 88]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)
print("\nFirst 5 rows:\n", df.head())
print("\nShape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nStatistical Summary:\n", df.describe())
print("\nCorrelation:\n", df[['Age', 'Marks']].corr())
