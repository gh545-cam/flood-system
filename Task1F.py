
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    stations = build_station_list()
    res = inconsistent_typical_range_stations(stations)
    lst = []
    for item in res:
        lst.append(item.name)
    print(lst)


if __name__ == "__main__":
    run()