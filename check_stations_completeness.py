'''
Author: CHRN

Date: May 3, 2025
'''

#%% Import functions
from bmkg_helper_functions import *

#%% Local functions

def find_duplicates(input_list: list) -> list:
    '''List duplicated items in a list'''
    seen = set()
    duplicates = set()

    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

#%% Define all station names (collected from website)
station_names = ["Balai Besar Meteorologi Klimatologi dan Geofisika Wilayah I", "Balai Besar Meteorologi Klimatologi dan Geofisika Wilayah III", 
                "Balai Besar Meteorologi Klimatologi dan Geofisika Wilayah IV", "Halim Perdana Kusuma Jakarta", "Pos Meteorologi Majene", 
                "Pos Meteorologi Penggung", "Pos Pengamatan Kahang-Kahang", "Stasiun Geofisika Aceh Besar", "Stasiun Geofisika Aceh Selatan", 
                "Stasiun Geofisika Alor", "Stasiun Geofisika Ambon", "Stasiun Geofisika Balikpapan", "Stasiun Geofisika Bandung", 
                "Stasiun Geofisika Banjarnegara", "Stasiun Geofisika Deli Serdang", "Stasiun Geofisika Denpasar", "Stasiun Geofisika Gorontalo", 
                "Stasiun Geofisika Gowa", "Stasiun Geofisika Gunungsitoli", "Stasiun Geofisika Jayapura", "Stasiun Geofisika Kendari", 
                "Stasiun Geofisika Kepahiang", "Stasiun Geofisika Kupang", "Stasiun Geofisika Lampung Utara", "Stasiun Geofisika Malang", 
                "Stasiun Geofisika Maluku Tenggara Barat", "Stasiun Geofisika Manado", "Stasiun Geofisika Nabire", "Stasiun Geofisika Nganjuk", 
                "Stasiun Geofisika Padang Panjang", "Stasiun Geofisika Palu", "Stasiun Geofisika Pasuruan", "Stasiun Geofisika Sleman", 
                "Stasiun Geofisika Sorong", "Stasiun Geofisika Sumba Timur", "Stasiun Geofisika Tangerang", "Stasiun Geofisika Tanjung Pandan", 
                "Stasiun Geofisika Ternate", "Stasiun Klimatologi Aceh", "Stasiun Klimatologi Bali", "Stasiun Klimatologi Bangka Belitung", 
                "Stasiun Klimatologi Banten", "Stasiun Klimatologi Bengkulu", "Stasiun Klimatologi DI Yogyakarta", "Stasiun Klimatologi Gorontalo", 
                "Stasiun Klimatologi Jambi", "Stasiun Klimatologi Jawa Barat", "Stasiun Klimatologi Jawa Tengah", "Stasiun Klimatologi Jawa Timur", 
                "Stasiun Klimatologi Jayapura", "Stasiun Klimatologi Kalimantan Barat", "Stasiun Klimatologi Kalimantan Selatan", 
                "Stasiun Klimatologi Lampung", "Stasiun Klimatologi Maluku", "Stasiun Klimatologi Merauke", "Stasiun Klimatologi Nusa Tenggara Barat", 
                "Stasiun Klimatologi Nusa Tenggara Timur", "Stasiun Klimatologi Papua Barat", "Stasiun Klimatologi Riau", 
                "Stasiun Klimatologi Sulawesi Selatan", "Stasiun Klimatologi Sulawesi Tenggara", "Stasiun Klimatologi Sulawesi Utara", 
                "Stasiun Klimatologi Sumatera Barat", "Stasiun Klimatologi Sumatera Selatan", "Stasiun Klimatologi Sumatera Utara", 
                "Stasiun Meteorologi Aek Godang", "Stasiun Meteorologi Ahmad Yani", "Stasiun Meteorologi Aji Pangeran Tumenggung Pranoto", 
                "Stasiun Meteorologi Amahai", "Stasiun Meteorologi Andi Jemma", "Stasiun Meteorologi Bandaneira", "Stasiun Meteorologi Banyuwangi", 
                "Stasiun Meteorologi Beringin", "Stasiun Meteorologi Beto Ambari", "Stasiun Meteorologi Binaka", "Stasiun Meteorologi Budiarto", 
                "Stasiun Meteorologi Citeko", "Stasiun Meteorologi Cut Nyak Dhien Nagan Raya", "Stasiun Meteorologi Dabo", 
                "Stasiun Meteorologi David Constatijn Saudale", "Stasiun Meteorologi Depati Amir", "Stasiun Meteorologi Depati Parbo", 
                "Stasiun Meteorologi Dhoho", "Stasiun Meteorologi Djalaluddin", "Stasiun Meteorologi Dok II Jayapura", 
                "Stasiun Meteorologi Domine Eduard Osok", "Stasiun Meteorologi Eltari", "Stasiun Meteorologi Emalamo", 
                "Stasiun Meteorologi Enarotali", "Stasiun Meteorologi Fatmawati Soekarno", "Stasiun Meteorologi FL Tobing", 
                "Stasiun Meteorologi Fransiskus Xaverius Seda", "Stasiun Meteorologi Frans Kaisiepo", "Stasiun Meteorologi Frans Sales Lega", 
                "Stasiun Meteorologi Gamar Malamo", "Stasiun Meteorologi Gewayantana", "Stasiun Meteorologi Gusti Syamsir Alam", 
                "Stasiun Meteorologi Hang Nadim", "Stasiun Meteorologi H. Asan", "Stasiun Meteorologi H. AS. Hanandjoeddin", 
                "Stasiun Meteorologi I Gusti Ngurah Rai", "Stasiun Meteorologi Iskandar", "Stasiun Meteorologi Japura", 
                "Stasiun Meteorologi Juanda", "Stasiun Meteorologi Juwata", "Stasiun Meteorologi Kalimarau", 
                "Stasiun Meteorologi Karel Sadsuitubun", "Stasiun Meteorologi Kasiguncu", "Stasiun Meteorologi Kemayoran", 
                "Stasiun Meteorologi Kertajati", "Stasiun Meteorologi Komodo", "Stasiun Meteorologi Kualanamu", "Stasiun Meteorologi Kuffar", 
                "Stasiun Meteorologi Maimun Saleh", "Stasiun Meteorologi Mali", "Stasiun Meteorologi Malikussaleh", "Stasiun Meteorologi Mararena", 
                "Stasiun Meteorologi Maritim Ambon", "Stasiun Meteorologi Maritim Belawan", "Stasiun Meteorologi Maritim Bitung", 
                "Stasiun Meteorologi Maritim Kendari", "Stasiun Meteorologi Maritim Panjang", "Stasiun Meteorologi Maritim Paotere", 
                "Stasiun Meteorologi Maritim Pontianak", "Stasiun Meteorologi Maritim Serang", "Stasiun Meteorologi Maritim Tanjung Emas", 
                "Stasiun Meteorologi Maritim Tanjung Perak", "Stasiun Meteorologi Maritim Tanjung Priok", "Stasiun Meteorologi Maritim Tegal", 
                "Stasiun Meteorologi Maritim Teluk Bayur", "Stasiun Meteorologi Maritim Tenau", "Stasiun Meteorologi Mathilda Batlayeri", 
                "Stasiun Meteorologi Minangkabau", "Stasiun Meteorologi Mopah", "Stasiun Meteorologi Mozez Kilangin", 
                "Stasiun Meteorologi Mutiara Sis-Al Jufri", "Stasiun Meteorologi Nabire", "Stasiun Meteorologi Naha", "Stasiun Meteorologi Namlea", 
                "Stasiun Meteorologi Nangapinoh", "Stasiun Meteorologi Nunukan", "Stasiun Meteorologi Oesman Sadik", "Stasiun Meteorologi Paloh", 
                "Stasiun Meteorologi Pangsuma", "Stasiun Meteorologi Pattimura", "Stasiun Meteorologi Perak I", "Stasiun Meteorologi Radin Inten II", 
                "Stasiun Meteorologi Rahadi Oesman", "Stasiun Meteorologi Raja Haji Abdullah", "Stasiun Meteorologi Raja Haji Fisabilillah", 
                "Stasiun Meteorologi Ranai", "Stasiun Meteorologi Rendani", "Stasiun Meteorologi Sam Ratulangi", "Stasiun Meteorologi Sanggu", 
                "Stasiun Meteorologi Sangia Ni Bandera", "Stasiun Meteorologi Sangkapura", "Stasiun Meteorologi Sentani", "Stasiun Meteorologi Silangit", 
                "Stasiun Meteorologi Soekarno Hatta", "Stasiun Meteorologi Sudjarwo Tjondro Negoro", "Stasiun Meteorologi Sultan Aji Muhammad Sulaiman Sepinggan", 
                "Stasiun Meteorologi Sultan Babullah", "Stasiun Meteorologi Sultan Bantilan", "Stasiun Meteorologi Sultan Hasanuddin", 
                "Stasiun Meteorologi Sultan Iskandar Muda", "Stasiun Meteorologi Sultan Mahmud Badaruddin II", "Stasiun Meteorologi Sultan Muhammad Kaharuddin", 
                "Stasiun Meteorologi Sultan Muhammad Salahuddin", "Stasiun Meteorologi Sultan Syarif Kasim II", "Stasiun Meteorologi Sultan Thaha", 
                "Stasiun Meteorologi Supadio", "Stasiun Meteorologi Syamsudin Noor", "Stasiun Meteorologi Syukuran Aminudin Amir", 
                "Stasiun Meteorologi Tampa Padang Mamuju", "Stasiun Meteorologi Tanah Merah", "Stasiun Meteorologi Tanjung Harapan", 
                "Stasiun Meteorologi Tardamu", "Stasiun Meteorologi Tarempa", "Stasiun Meteorologi Tebelian", "Stasiun Meteorologi Tjilik Riwut", 
                "Stasiun Meteorologi Toraja", "Stasiun Meteorologi Torea", "Stasiun Meteorologi Trunojoyo", "Stasiun Meteorologi Tuban", 
                "Stasiun Meteorologi Tunggul Wulung", "Stasiun Meteorologi Umbu Mehang Kunda", "Stasiun Meteorologi Utarom", 
                "Stasiun Meteorologi Wamena Jaya Wijaya", "Stasiun Meteorologi Yogyakarta", "Stasiun Meteorologi Yuvai Semaring", 
                "Stasiun Meteorologi Zainuddin Abdul Madjid", "Stasiun Pemantau Atmosfer Global Bukit Koto Tabang", 
                "Stasiun Pemantau Atmosfer Global Lore Lindu Bariri", "Stasiun Pemantau Atmosfer Global Puncak Vihara Klademak", 
                "Taman Alat Digital Staklim Sumsel"]

print('Number of available stations in website:', len(set(station_names)))

#%% Collect station names from downloaded data

# List Excel files' path
data_path = r'/home/nathasya/Documents/Witteveen Bos 2024-2025/Data/BMKG Raw Data 2025'
excel_files = list_excel_files_path(data_path)

# Save station names
available_station_name = []
for path in excel_files:
    station_dict = read_excel_file_for_station_info(path)
    available_station_name.append(station_dict['name'])

print('Number of obtained stations:', len(set(available_station_name)))
duplicates = find_duplicates(available_station_name)
print("Duplicated obtained stations:", duplicates)

#%% Check whether each station has been downloaded
unavailable_station_names = []
for station_name in set(station_names):
    if station_name not in set(available_station_name):
        unavailable_station_names.append(station_name)

# Print findings
print(f'There are {len(unavailable_station_names)} stations which have not been downloaded:')
for name in unavailable_station_names:
    print(name)

#%% Check completeness of each obtained data

# Read each data
available_station_df = []
for path in excel_files:
    df = read_excel_file_for_data(path)
    available_station_df.append(df)

# Iterate over each station and save problem info
problematic_station_names = []
problematic_logs = []
for idx, df in enumerate(available_station_df):
    name = available_station_name[idx]
    try:
        variables_are_complete, unavailable_col_names, is_more_than_10_years = check_data_completeness(df)
        # Print out info
        if (not variables_are_complete) or (not is_more_than_10_years):
            
            if (not variables_are_complete) and (not is_more_than_10_years):
                log = 'Vars are not complete, length is less than 10 years'
            elif (not variables_are_complete):
                log = 'Vars are not complete'
            else:
                log = 'Length is less than 10 years'
        else:
            log = None
    except:
        log = 'File format is wrong'
    if log != None:
        problematic_station_names.append(name)
        problematic_logs.append(log)
# Print problem
df_problem_log = pd.DataFrame({'station_name': problematic_station_names, 'log': problematic_logs})
df_problem_log.to_excel('Data cleaning problem logs.xlsx', index=False)