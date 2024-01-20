from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
def run():
    stations = build_station_list()
    lst = stations_within_radius(stations,(52.2053, 0.1218),10)
    res = []
    for item in lst:
        res.append(item.name)
    print(res)

if __name__ == "__main__":
    run()