# Import package
import xarray as xr

# Read data
path = r"C:\Users\CHRN\OneDrive - Witteveen+Bos\Climate Resilience\Water Management\BMKG meteo database\bmkg_2025.nc"
ds = xr.open_dataset(path)

# Filter by station name
chosen_station = 'Halim Perdana Kusuma Jakarta'
station_id = ds['station_name'].where(ds['station_name'] == chosen_station, drop=True)['station'].values
ds['RR'].sel(station=station_id).plot()