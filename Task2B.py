from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    #retrieve stations with water level over 0.8 tolerance
    lst = stations_level_over_threshold(stations,0.8)
    #print station name and relative water level
    for (station,level) in lst:
        print(station.name,level)

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()