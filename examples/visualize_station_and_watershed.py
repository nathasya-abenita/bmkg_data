"""
Plot BMKG stations and watershed boundaries in one map

Author: CHRN
Date: May 3, 2025
"""

import xarray as xr
import geopandas as gpd
import pandas as pd
import contextily as cx
import matplotlib.pyplot as plt
from shapely import Point

def create_gdf (list):
    '''
    Convert a list of stations profile to GeoDataFrame.
    A station profile must be [lon, lat, station_name] and saved in the list.
    '''
    df = pd.DataFrame({'name': [loc[2] for loc in list],
              'geometry': [Point(loc[1], loc[0]) for loc in list]})
    gdf = gpd.GeoDataFrame(df, geometry=df['geometry'], crs='EPSG:4326')
    return gdf

# Read BMKG stations shapefile
bmkg_shp_path = r"C:\Users\CHRN\OneDrive - Witteveen+Bos\Climate Resilience\Water Management\BMKG meteo database\BMKG Stations Shapefile\bmkg_2025.shp"
gdf_bmkg = gpd.read_file(bmkg_shp_path)

# Read watershed shapefile
watershed_shp_path = r'C:\Users\CHRN\OneDrive - Witteveen+Bos\Climate Resilience\Water Management\BMKG meteo database\Indonesia Watershed Shapefile\Batas_DAS_KLHK.zip'
gdf_watershed = gpd.read_file(watershed_shp_path).to_crs(crs=gdf_bmkg.crs)

# Initialize figure
fig, ax = plt.subplots(figsize=(12,6))

# Plot watershed boundaries
gdf_watershed.boundary.plot(ax=ax, color='k', label='Watershed Boundaries', linewidth=1, zorder=1)

# Plot BMKG stations
gdf_bmkg.plot(ax=ax, color='tab:red', label='Available BMKG Stations', markersize=5, zorder=2)

# Plot limits
bounds = gdf_watershed.total_bounds
x_diff = 3
y_diff = 3
plt.xlim([bounds[0] - x_diff, bounds[2] + x_diff])
plt.ylim([bounds[1] - y_diff, bounds[3] + y_diff])

# Add basemap
cx.add_basemap(ax=ax, source=cx.providers.Esri.WorldImagery, crs=gdf_bmkg.crs, zorder=0)

# Plot decorators
plt.legend()
plt.title('BMKG Stations Location with Indonesian Watershed Boundaries')
plt.xlabel('Lon [Degrees]'); plt.ylabel('Lat [Degrees]')

# Show plot
# plt.show()

# Save figure
plt.savefig('BMKG Stations and Watershed Boundaries.png')