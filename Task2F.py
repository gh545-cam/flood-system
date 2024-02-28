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

def run():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    # Print station and latest level for first 5 stations in list
    res = stations_level_over_threshold(stations,0)
    i = 0
    while i < 5:
        station = res[i][0]
        dt = 2
        dates,levels = fetch_measure_levels(station.measure_id,dt = datetime.timedelta(days=dt))
        if dates == []:
            i+= 1
            continue
        d = matplotlib.dates.date2num(dates)
        plot_water_level_with_fit(station, dates, levels, 4)
        i += 1


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
