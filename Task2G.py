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
    dic = {"Severe":[],'High':[],'Moderate':[],'Low':[]}
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    for station in stations:
        #check that station has consistent typical range
        if station.typical_range_consistent() == True:
            level = station.relative_water_level()
            #obtain relative water level
            continue
    #conduct gradient analysis
        dt = 2
        dates,levels = fetch_measure_levels(station.measure_id,dt = datetime.timedelta(days=dt))
        if dates != [] and levels != []:
            #check dates and levels are not empty
            date_float = matplotlib.dates.date2num(dates)
            p_coeff = np.polyfit(date_float-date_float[0], levels, 4)
            poly = np.poly1d(p_coeff)
            #obtain polynomial fit
            fderiv = poly.deriv()
            #find derivative
            grad = fderiv(date_float-date_float[0])[-1]
            #latest gradient = last item of derivative list
            town = station.town
            #get station town name
            if station.town == None:
                continue
            #sort towns into categories based on aforementioned restrictions
            if level >= 0.8:
                if town not in dic['Severe']:
                    dic['Severe'].append(town)
            elif level >= 0.5 and level < 0.8 and grad > 0:
                if town not in dic['High']:
                    dic['High'].append(town)
            elif level < 0.8 and level >= 0.5 and grad < 0:
                if town not in dic['Moderate']:
                    dic['Moderate'].append(town)
            else:
                if town not in dic['Low']:
                    dic['Low'].append(town)
        print(dic)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
