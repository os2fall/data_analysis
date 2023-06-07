import urllib, urllib.request
from datetime import datetime
import glob
import os.path

def get_data(province_id):
    url="https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?country=UKR&provinceID={}&year1=1981&year2=2023&type=Mean".format(province_id)
    
    webpage = urllib.request.urlopen(url)
    text = webpage.read()
    now = datetime.now()
    date_and_time_time = now.strftime("%d.%m.%Y_%H^%M^%S")
    out = open('C:\\Study\\AD\\lab1\\' + 'NOAA_ID' + str(province_id) + '-' + date_and_time_time + '.csv', 'wb')
    out.write(text)
    out.close
    
import pandas as pd

def make_header(filepath):
    headers = ['Year', 'Week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI', 'empty']
    dataframe = pd.read_csv(filepath, header=1, names=headers)
    dataframe.drop(dataframe.loc[dataframe['VHI'] == -1].index)
    return dataframe

def index_change(filepath, old, new, oblast):
    dataframe = make_header(filepath)

    dataframe['area'] = old
    dataframe['area'].replace({old: new}, inplace=True)

    dataframe.to_csv(f'C:\\Study\\AD\\lab1\\NOAA_ID{new} {oblast}).csv', index=False)
    return dataframe

def data_analysis(filepath, year):
    data = pd.read_csv(filepath)
    df = data[data['VHI'] != -1]

    ext_drought = df[df['VHI'] <= 15]  # Data for extreme drought periods
    max_val = ext_drought.loc[ext_drought['Year'].astype(str) == str(year), 'VHI'].max()
    print(f"{max_val} - maximum VHI for extreme drought in {year}")
    min_val = ext_drought.loc[ext_drought['Year'].astype(str) == str(year), 'VHI'].min()
    print(f"\t{min_val} - minimum VHI for extreme drought in {year}")

    this_year = int(ext_drought.loc[ext_drought['VHI'].idxmin(), 'Year'])
    print(f"\t\t{this_year} - the year with the most extreme drought period")

    drought = df[(15 < df['VHI']) & (df['VHI'] <= 35)]  # Data for moderate drought periods
    min_val = drought.loc[drought['Year'].astype(str) == str(year), 'VHI'].min()
    print(f"\t{min_val} - minimum VHI for moderate drought in {year}")
    max_val = drought.loc[drought['Year'].astype(str) == str(year), 'VHI'].max()
    print(f"{max_val} - maximum VHI for moderate drought in {year}")

            
data_analysis("C:\\Study\\AD\lab1\\NOAA_ID1 Волинська).csv", 2000)