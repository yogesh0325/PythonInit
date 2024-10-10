import pandas as pd
from shapely import wkb

# Step 1: Read the Parquet file using pandas
df = pd.read_parquet('./example.parquet')
pd.set_option('display.max_colwidth', None)
column_names = df.columns
# Step 2: Convert the 'geometry' column (which contains WKB) to WKT using shapely
# Create a new column with the WKT values
df['geometry_wkt'] = df['parcel_geometry'].apply(lambda x: wkb.loads(x).wkt)

# Step 3: Display the DataFrame or save the output
print(df[['geometry_wkt']])  # Display the WKT column

# Save the DataFrame with WKT column to a CSV file if needed
# df.to_csv('output_with_wkt.csv', index=False)
# Index(['geometry', 'imagery_date', 'imagery_source', 'parcel_geometry'], dtype='object')