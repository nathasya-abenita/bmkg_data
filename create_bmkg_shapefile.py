"""
Create BMKG stations location shapefile

Author: CHRN
Date: June 2025
"""

import xarray as xr
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

# Read data
nc_path = r'./output/bmkg_2025_final.nc'
ds = xr.open_dataset(nc_path)

# Prepare DataFrame for the stations info
df = pd.DataFrame({
    "id_wmo": ds["station"].values,
    "station_name": ds["station_name"].values,
    "latitude": ds["latitude"].values,
    "longitude": ds["longitude"].values,
    "elevation": ds["elevation"].values
})

# Create a geometry column using Point objects
df["geometry"] = df.apply(lambda row: Point(row["longitude"], row["latitude"]), axis=1)

# Convert DataFrame to GeoDataFrame and set the coordinate reference system (CRS) to WGS84
gdf = gpd.GeoDataFrame(df, geometry="geometry", crs="EPSG:4326")

# Rename column
gdf = gdf.rename(columns={'station_name': 'name'})

# Export
gdf.to_file(filename=r'./output/shp/bmkg_2025.shp')