import pandas as pd

data = {
    'Name': ['Akshay', 'Rahul', 'Priya', 'Neha'],
    'Marks': [88, 76, 91, 84]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)
print("\nFirst rows:\n", df.head())
print("\nStudents with marks above 80:\n", df[df['Marks'] > 80])

# Add a new column
df['Result'] = df['Marks'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
print("\nUpdated DataFrame:\n", df)

print("\nAverage Marks:", df['Marks'].mean())
