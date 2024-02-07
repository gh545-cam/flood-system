from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
def run():
    #prints all station names within given radius of given center coordinates
    stations = build_station_list()
    lst = stations_within_radius(stations,(52.2053, 0.1218),10)
    res = []
    for item in lst:
        res.append(item.name)
        #extract and append station name to result list from station object
    res.sort()
    print(res)

if __name__ == "__main__":
    run()