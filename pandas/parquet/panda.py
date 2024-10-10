import pandas as pd
df = pd.read_parquet('./example.parquet')
# df = pd.read_parquet('./example.parquet', columns=['geometry'])
pd.set_option('display.max_colwidth', None)
print(df.columns)
print(df.head())
row_index  = 0
print('~~~~~~~~~~')
print(str(df.loc[row_index, 'geometry']))
