#%% Import packages and functions

from bmkg_helper_functions import *

#%% Main program

# Inputs
output_file = 'bmkg_2025_final.nc'
data_folder_path = r'C:\Users\CHRN\OneDrive - Witteveen+Bos\Climate Resilience\Water Management\BMKG meteo database\Raw Data'

# Read Excel file paths
excel_files = list_excel_files_path(data_folder_path)

# Obtain station info dictionary
station_dict_list = []
station_df_list = []

for path in excel_files:
    # Obtain dictionary
    station_dict = read_excel_file_for_station_info(path)
    df = read_excel_file_for_data(path)

    # Try to clean and save if possible
    try:
        # Try to clean
        df_clean = clean_data(df)

        # Append to list
        station_dict_list.append(station_dict)
        station_df_list.append(df_clean)
    except:
        # Print warning
        name = station_dict['name']
        print(f"Failed to read and clean this station's file: {name}")

        # Create empty DataFrame
        # df_clean = pd.DataFrame(columns=['TN', 'TX', 'TAVG', 'RH_AVG', 'RR', 'SS', 'FF_X', 'DDD_X', 'FF_AVG', 'DDD_CAR'])

        # Append to list
        # station_dict_list.append(station_dict)
        # station_df_list.append(df_clean)

# Export as NC file
placeholder_output_file = 'placeholder' + output_file
ds = create_netcdf(station_dict_list, station_df_list, placeholder_output_file)

# Resolving known issue, SS variable is exported for the first time as datetime object
ds_new = xr.open_dataset(placeholder_output_file)   # read exported file
ds_new['SS'].data = ds['SS'].data                   # replace the SS variable with the correct values
ds_new.to_netcdf(output_file)                       # reexport the NC file