import pandas as pd

dataset = 'data/MSR_data_cleaned.csv'
chunksize = 10 ** 5
count = 0
total = 0
with pd.read_csv(dataset, chunksize=chunksize) as reader:
    for chunk in reader:
        vulCol = chunk['vul']
        print(vulCol.value_counts())


print(count)
