from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

def run():
    #returns 10 closest and 10 furthest stations measured from input coordinates
    stations = build_station_list()
    res = stations_by_distance(stations,(52.2053, 0.1218))
    closest = res[:10] #list of 10 station objects closest to input coordinates
    furthest = res[-11:] #list of 10 station objects furthest away from input coordinates
    c = []
    f = []
    for lst in closest:
        #extracts station name and town from station object, and compile with distance in tuple
        s = lst[0]
        c.append((s.name,s.town,lst[1]))
    for lst in furthest:
        #extracts station name and town from station object, and compile with distance in tuple
        s = lst[0]
        f.append((s.name,s.town,lst[1]))
    print('closest:',c)
    print('furthest:',f)


if __name__ == "__main__":
    run()