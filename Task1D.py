from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
def run():
    #print stations located in River Aire, Cam and Thames respectively
    stations = build_station_list()
    lst = list(rivers_with_station(stations))
    lst.sort()
    print(lst[:10])

    dic = stations_by_river(stations)
    #creates dictionary of river names as keys and list of stations as values
    r1 = []
    r2 = []
    r3 = []
    for item in dic['River Aire']:
        #extracts list of station objects from dictionary, then extract name from station object to append to output list
        r1.append(item)
    r1.sort()
    for item in dic['River Cam']:
        r2.append(item)
    r2.sort()
    for item in dic['River Thames']:
        r3.append(item)
    r3.sort()
    print(r1)
    print(r2)
    print(r3)



if __name__ == "__main__":
    run()