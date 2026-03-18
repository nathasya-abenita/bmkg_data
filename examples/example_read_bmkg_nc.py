# Import package
import xarray as xr
import matplotlib.pyplot as plt

# Read data
path = r"./output/bmkg_2025_final.nc"
ds = xr.open_dataset(path)

# Filter by station name
chosen_station = 'Halim Perdana Kusuma Jakarta'
station_id = ds['station_name'].where(ds['station_name'] == chosen_station, drop=True)['station'].values
ds['RR'].sel(station=station_id).plot()
plt.show()