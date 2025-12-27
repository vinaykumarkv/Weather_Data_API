from os import listdir
from os.path import isfile, join
import pandas as pd
import sqlite3
from sqlalchemy import create_engine

def check_db_present(folder_path):
    mypath = folder_path
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    if "weather_data.db" in onlyfiles:
        return True
    else:
        return False

def extract_clean_data(folder_path):
    mypath = folder_path
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    all_weather_dfs = []
    new_df = pd.DataFrame()
    for file in onlyfiles:
        if file == "stations.txt":
            stations_path = mypath + "stations.txt"
            stations_df = pd.read_csv(mypath + file, skiprows=17, sep=None, engine='python')
        else:
            new_df = pd.read_csv(mypath + file, skiprows=20, sep=None, engine='python')
            all_weather_dfs.append(new_df)
    all_weather_df = pd.concat(all_weather_dfs, axis=0, ignore_index=True)
    stations_df.columns = stations_df.columns.str.strip()
    all_weather_df.columns = all_weather_df.columns.str.strip()
    engine = create_engine(f'sqlite:///{mypath}weather_data.db')
    stations_df.to_sql('stations', con=engine, index=False, if_exists='replace')
    all_weather_df.to_sql('weather', con=engine, index=False, if_exists='replace')
    conn = sqlite3.connect(mypath+'weather_data.db')
    query = "SELECT count(*) FROM weather"
    result = pd.read_sql(query, conn)

    print(f"Database created with {result.shape[0]} rows in path : {mypath}/weather_data.db")
    conn.close()


def fetch_temperature(folder_path, station, date):
    # Use the folder_path to ensure we find the CORRECT .db file
    conn = sqlite3.connect(folder_path + 'weather_data.db')
    query = f"SELECT TG FROM weather WHERE STAID={int(station)} AND DATE={int(date)}"

    try:
        result_df = pd.read_sql(query, conn)
        conn.close()
        # Handle cases where no data is found for that station/date
        if result_df.empty:
            return "No data found"
        return str(result_df['TG'].iloc[0])
    except Exception as e:
        conn.close()
        return f"Error: {str(e)}"

def get_stations(folder_path):
    mypath = folder_path
    conn = sqlite3.connect(mypath+'weather_data.db')
    query = "SELECT STAID,STANAME,CN,LAT,LON,HGHT FROM stations"
    df = pd.read_sql(query, conn)
    conn.close()
    data = df.to_dict(orient='records')
    print(data)
    return data

