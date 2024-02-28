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
import numpy as np

def run():
    """Estimates gradient from previous i level measurements.
    Thresholds (Measured in relative water level:
    Severe: 2.5
    High: 2
    Moderate: 1.6
    Low: 1.25"""
    dic = {"Severe":[],'High':[],'Moderate':[],'Low':[]}
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.relative_water_level() == None:
            pass
        elif station.relative_water_level() >= 1.25:
            if station.town != None and station.typical_range_consistent() and station.town not in dic:
                dates,levels = fetch_measure_levels(station.measure_id,dt = datetime.timedelta(days=0.1))
                if dates != [] and levels != []:
                    #check dates and levels are not empty
                    level = station.relative_water_level()
                    #obtain relative water level
                    i=5 
                    latest_levels = levels[-i:-1]
                    gradient = np.diff(latest_levels)
                    average_gradient = gradient.sum()/(i-2)
                    double_gradient = np.diff(gradient)
                    average_double_gradient = double_gradient.sum()/(i-3)
                    if average_gradient > 0.02 or (average_gradient > 0 and average_double_gradient > 0):
                        state = "\033[1;31;40m Rising \033[1;37;40m"
                    elif average_gradient < -0.02 or (average_gradient < 0 and average_double_gradient < 0):
                        state = "\033[1;32;40m Falling \033[1;37;40m"
                    else:
                        state = "\033[1;33;40m Steady \033[1;37;40m"
                    town = station.town
                    #sort towns into categories based on aforementioned restrictions
                    if level >= 2.5:
                        if town not in dic['Severe']:
                            dic['Severe'].append(town + "      Water Level: " + state)
                    elif level >= 2.0:
                        if town not in dic['High']:
                            dic['High'].append(town + "      Water Level: " + state)
                    elif level >= 1.6:
                        if town not in dic['Moderate']:
                            dic['Moderate'].append(town + "      Water Level: " + state)
                    else:
                        if town not in dic['Low']:
                            dic['Low'].append(town + "      Water Level: " + state)
    print("Severe: \n\n", "\n".join(dic["Severe"]))
    print("\n High: \n\n", "\n".join(dic["High"]))
    print("\nModerate:\n\n", "\n".join(dic["Moderate"]))
    print("\nLow:\n\n", "\n".join(dic["Low"]))

if __name__ == "__main__":
    print("***\033[1;37;40m Task 2G: CUED Part IA Flood Warning System ***")
    run()
