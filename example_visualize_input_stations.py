"""
Plot BMKG stations and inputted station locations

Author: CHRN
"""

import xarray as xr
import geopandas as gpd
import pandas as pd
import contextily as cx
import matplotlib.pyplot as plt
from shapely import Point

#%% Functions

def create_gdf (list: list) -> gpd.GeoDataFrame:

    df = pd.DataFrame({'name': [loc[2] for loc in list],
              'geometry': [Point(loc[1], loc[0]) for loc in list]})
    gdf = gpd.GeoDataFrame(df, geometry=df['geometry'], crs='EPSG:4326')
    return gdf

#%% Inputs

# Define station locations [lat, lon, station_name]
station_locations = [
    [-1.431389, 120.315472, 'Stasiun Wuasa'],
    [-1.448722, 119.985444, 'Stasiun\n Kulawi'],
    [-1.796389, 120.017222, 'Stasiun\n Meteorologi\n Kalamanta'],
    [-1.530833, 120.328333, 'Stasiun\n Lore Piore'],
    [-1.833889, 120.339722, 'Stasiun\n Barita']
]

#%% Main program

# Read internal BMKG shapefile
bmkg_shp_path = r'C:\Users\CHRN\OneDrive - Witteveen+Bos\Climate Resilience\Water Management\BMKG meteo database\BMKG Stations Shapefile\bmkg_2025.shp'
gdf_bmkg = gpd.read_file(bmkg_shp_path)

# Create geodataframe for locations input
gdf_station = create_gdf(station_locations)

# Initialize plot
fig, ax = plt.subplots(figsize=(7,7))

# Plot locations
gdf_station.plot(ax=ax, color='tab:blue', label='Past Study Stations')

# Plot BMKG stations
gdf_bmkg.plot(ax=ax, color='tab:red', label='BMKG Stations')

# Add text station names
shift_y_text    = 0.02
for loc in station_locations:
    ax.text(loc[1], loc[0] - shift_y_text, loc[2], color='white', horizontalalignment='center', zorder=0.5, fontsize=6, verticalalignment='top')

for _, row in gdf_bmkg.iterrows():
    ax.text(row['longitude'], row['latitude'] + shift_y_text * 5, row['name'], color='white', horizontalalignment='center', zorder=0.5, fontsize=6, verticalalignment='top')

# Set limit
bounds = gdf_station.total_bounds
x_diff = 1.5
y_diff = 1.5
plt.xlim([bounds[0] - x_diff, bounds[2] + x_diff])
plt.ylim([bounds[1] - y_diff, bounds[3] + y_diff])

# Add basemap
cx.add_basemap(ax=ax, source=cx.providers.Esri.WorldImagery, crs='EPSG:4326')

# Add legend
plt.legend()

# Add title
plt.title('Previous Stations vs Available BMKG Stations')

# Axis labels
plt.xlabel('Lon [Degrees]'); plt.ylabel('Lat [Degrees]')

plt.show()