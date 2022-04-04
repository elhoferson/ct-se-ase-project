import pandas as pd

chunk = 'data/MSR_chunk_11.csv'

df = pd.read_csv(chunk)
print(df.head())

