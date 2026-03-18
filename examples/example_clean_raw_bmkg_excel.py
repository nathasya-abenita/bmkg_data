"""
Example: Clean Raw BMKG Excel File

Author: CHRN
Date: July 2025
"""

# Import package
import sys, os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bmkg_helper_functions import *

# Define path to raw Excel file
excel_path = r'sample_data\Stasiun Meteorologi Maritim Tenau.xlsx'

# Obtain dictionary
station_dict = read_excel_file_for_station_info(excel_path)
print('Station info:\n', station_dict)

# Read data as DataFrame
df = read_excel_file_for_data(excel_path)

# Try to clean data if possible
try:
    # Try to clean
    df_clean = clean_data(df)
    print('Cleaned data:\n', df_clean)
except Exception as e:
    # Print warning
    name = station_dict['name']
    print(f"Failed to read and clean this station's file: {name}")
    print(f'Error message: {e}')