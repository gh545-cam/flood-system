#define risk levels as:
# severe:
    # rel. levels >= 0.8
# high:
    # rel. levels between 0.5 and 0.8, positive gradient
# moderate:
    # rel. levels between 0.5 and 0.8, negative gradient
# low:
    # rel. levels less than 0.5

# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
import matplotlib
from floodsystem.flood import stations_level_over_threshold
from floodsystem.utils import sorted_by_key
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels


def run():
    dic = {"Severe":[],'High':[],'Moderate':[],'Low':[]}
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    for station in stations:
    # Split stations based on threshold (0.8 and 0.5)
        if station.typical_range_consistent() == True:
            level = station.relative_water_level()

    #conduct gradient analysis
        dt = 2
        dates,levels = fetch_measure_levels(station.measure_id,dt = datetime.timedelta(days=dt))
        if dates != [] and levels != []:
            d = matplotlib.dates.date2num(dates)
            grad = (levels[0]-levels[-1])/(d[0]-d[-1])
            town = station.town
            if level >= 0.8:
                if town not in dic['Severe']:
                    dic['Severe'].append(town)
            elif level >= 0.5 and level < 0.8 and grad > 0:
                    dic['High'].append(town)
            elif level < 0.8 and level >= 0.5 and grad < 0:
                if town not in dic['Moderate']:
                    dic['Moderate'].append(town)
            else:
                if town not in dic['Low']:
                    dic['Low'].append(town)
        print(dic)



        
    
    

if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()
