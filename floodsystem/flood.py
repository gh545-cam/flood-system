from . import datafetcher
from .station import MonitoringStation
from .utils import sorted_by_key


def stations_level_over_threshold(stations,tol):
    res = []
    for station in stations:
        bol = station.typical_range_consistent()
        if bol == True:
            level = station.relative_water_level()
            if level != None and level > tol:
                res.append((station,level))
    result = sorted_by_key(res,1)
    return result

def stations_highest_rel_level(stations,N):
    res = stations_level_over_threshold(stations,0)
    lst = []
    i = len(lst)
    while len(lst) < N:
        s = res[len(res) - 1 - len(lst)][0]
        lst.append((s,res[len(res)-1-len(lst)][1]))
    return lst

        
