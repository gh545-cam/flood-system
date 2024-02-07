
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    #print list of stations with inconsistent ranges usingg inconsistent_typical_range_station function
    stations = build_station_list()
    res = inconsistent_typical_range_stations(stations)
    res.sort()
    print(res)


if __name__ == "__main__":
    run()