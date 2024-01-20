from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

def run():
    stations = build_station_list()
    res = rivers_by_station_number(stations,9)
    print(res)


if __name__ == "__main__":
    run()