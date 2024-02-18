# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels


def run():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    # Obtain station and latest level for first 5 stations with highest rel. water level
    lst = stations_highest_rel_level(stations,5)

    #for each station in lst, fetch water level against time data and plot on interval of 10 days
    for tup in lst:
        station = tup[0]
        dt = 10
        dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station,dates,levels)


if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()
