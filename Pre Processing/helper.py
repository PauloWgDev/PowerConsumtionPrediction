import numpy as np
import pandas as pd


# Dictionary mapping Romanized names to file paths
stations_data = {
    "wugu": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 五股 _ csv_1.csv",
    "dounan": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 斗南 _ csv_15.csv",
    "yilan": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 宜蘭 _ csv_12.csv",
    "banchiao": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 板橋 _ csv.csv",
    "nantou": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 南投 _ csv_7.csv",
    "hengchun": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 恆春 _ csv_8.csv",
    "miaoli": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 苗栗 _ csv_5.csv",
    "yuanlin": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 員林 _ csv_16.csv",
    "taoyuan": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 桃園 _ csv_4.csv",
    "kaohsiung": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 高雄 _ csv_11.csv",
    "keelung": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 基隆 _ csv_3.csv",
    "shenkeng": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 深坑 _ csv.csv",
    "dongqu": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 新竹市東區 _ csv.csv",
    "chiayi": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 嘉義 _ csv_9.csv",
    "taichung": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 臺中 _ csv_6.csv",
    "taipei": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 臺北 _ csv_2.csv",
    "tainan": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 臺南 _ csv_13.csv",
    "suao": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 蘇澳 _ csv_10.csv",
    "linluo": "../Raw Data/Meteorological Data/逐日平均氣溫年報表_2024 麟洛 _ csv_14.csv"
}

stations_locations = {
    "wugu": (25.076227777777778, 121.41905277777778),
    "dounan": (23.680477777777778, 120.47023055555556),
    "yilan": (24.765791666666665, 121.74834166666666),
    "banchiao": (25.012430555555557, 121.4406388888889),
    "nantou": (23.913208333333333, 120.67918333333334),
    "hengchun": (22.00566111111111, 120.73830833333334),
    "miaoli": (24.566666666666666, 120.81644444444444),
    "yuanlin": (23.948055555555555, 120.57777777777777),
    "taoyuan": (24.99416666666667, 121.315),
    "kaohsiung": (22.73217222222222, 120.3044361111111),
    "keelung": (25.135130555555556, 121.7322638888889),
    "shenkeng": (25.00448888888889, 121.62010555555555),
    "dongqu": (24.80043888888889, 120.97873611111112),
    "chiayi": (23.497672222222224, 120.42478333333334),
    "taichung": (24.147494444444444, 120.6759138888889),
    "taipei": (25.039461111111113, 121.50664722222223),
    "tainan": (22.99501388888889, 120.196825),
    "suao": (24.59875, 121.84889444444444),
    "linluo": (22.652555555555555, 120.51913888888889)
}


def load_metereological_data_path(path):
    data = pd.read_csv(
    path,
    skiprows=5,             # skip the metadata rows
    header=0,               # use the first non-skipped row as the header
    encoding="utf-8-sig",
    index_col=0
    )
    data = data.iloc[:, :-1]
    return data

def load_metereological_data_city(city):
    path = stations_data[city]
    return load_metereological_data_path(path)
    

def load_metereological_data_all():
    data_frames = {}
    for city in stations_data:
        data = load_metereological_data_city(city=city)
        data_frames[city] = data
    return data_frames

print("Helper code loaded")