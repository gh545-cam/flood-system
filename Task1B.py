from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

def run():
    stations = build_station_list()
    res = stations_by_distance(stations,(52.2053, 0.1218))
    closest = res[:10]
    furthest = res[-11:]
    c = []
    f = []
    for lst in closest:
        s = lst[0]
        c.append((s.name,s.town,lst[1]))
    for lst in furthest:
        s = lst[0]
        f.append((s.name,s.town,lst[1]))
    print('closest:',c)
    print('furthest:',f)


if __name__ == "__main__":
    run()