import pandas as pd

dataset = 'data/processed_data.csv'
second_chunk = 'data/MSR_second_chunk{}.csv'
chunksize = 10 ** 4
count = 0
total = 0
with pd.read_csv(dataset, chunksize=chunksize) as reader:
    i = 1
    for chunk in reader:
        chunk.to_csv(f'data/MSR_processed_chunk_{i}.csv', sep=',')
        i += 1

print('finish')
