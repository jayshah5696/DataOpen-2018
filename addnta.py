import pandas as pd
import numpy as np
import os
import sys
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import multiprocessing as mp

df = pd.read_csv("geographic.csv")
df_uber_2014 = pd.read_csv("uber_trips_2014.csv")


def get_tuples(l, n=2):
    """Yield successive n-sized chunks from l."""
    return [l[i:i + n] for i in range(0, len(l), n)]


class NTA:
    def __init__(self, polygon, name):
        self.polygon = polygon
        self.name = name


all_ntas = []
for nta_name in df.columns:
    coords = np.array(df[nta_name])
    coords = coords[~np.isnan(coords)]
    poly = Polygon(get_tuples(coords))
    nta = NTA(poly, nta_name)
    all_ntas.append(nta)

# lon should be around -73
# lat should be around 40
def get_nta_from_gps(lon, lat):
    point = Point(lon, lat)
    for my_nta in all_ntas:
        if my_nta.polygon.contains(point):
            return my_nta.name
        


def get_code(i):
	lt = df_uber_2014["pickup_latitude"].iloc[i]
    ln = df_uber_2014["pickup_longitude"].iloc[i]
    if get_nta_from_gps(ln,lt) != None:
        code = get_nta_from_gps(ln,lt)
        return 
    else:
        return np.nan


pool = mp.Pool(processes=4)
nta_code_data = pool.map(get_code, range(len(df_uber_2014)))


# nta_code_data = []
# for i in range(len(df_uber_2014)):
#     lt = df_uber_2014["pickup_latitude"].iloc[i]
#     ln = df_uber_2014["pickup_longitude"].iloc[i]
#     if get_nta_from_gps(ln,lt) != None:
#         code = get_nta_from_gps(ln,lt)
#         nta_code_data.append(code)
#     else:
#         nta_code_data.append(np.nan)
    #print get_nta_from_gps(ln,lt)

df_uber_2014["NTA Code"] = nta_code_data
df_uber_2014.to_csv("uber_trips_2014_and_nta.csv")
