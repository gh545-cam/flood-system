from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    #retrieves top 10 stations with highest relative water level
    lst = stations_highest_rel_level(stations,10)
    #prints stations name and rel. water level in tuple form
    for (station,level) in lst:
        print((station.name,level))

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()