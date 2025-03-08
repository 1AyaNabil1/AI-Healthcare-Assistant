import pandas as pd
df = pd.read_csv('../Data/Raw/Symptom2Disease.csv')
print(df.head())
print(df.shape)
print(df['label'].value_counts())
print(df.isnull().sum())