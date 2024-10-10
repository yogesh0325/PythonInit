import pandas as pd
from shapely import wkb

# Assuming 'geometry' column contains WKB data
# Convert binary WKB data to a shapely geometry object
df = pd.read_parquet('./example.parquet')
geometry_wkb_m = df.loc[0, 'geometry']

# Decode the WKB to a geometry object
geometry_object = wkb.loads(geometry_wkb_m)

# Convert the geometry to WKT (Well-Known Text) format for readability
print(geometry_object.wkt)
# Index(['geometry', 'imagery_date', 'imagery_source', 'parcel_geometry'], dtype='object')