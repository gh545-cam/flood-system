from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
def run():
    stations = build_station_list()
    lst = list(rivers_with_station(stations))
    lst.sort()
    print(lst[:10])

    dic = stations_by_river(stations)
    r1 = []
    r2 = []
    r3 = []
    for item in dic['River Aire']:
        r1.append(item.name)
    r1.sort()
    for item in dic['River Cam']:
        r2.append(item.name)
    r2.sort()
    for item in dic['River Thames']:
        r3.append(item.name)
    r3.sort()
    print(r1)
    print(r2)
    print(r3)



if __name__ == "__main__":
    run()