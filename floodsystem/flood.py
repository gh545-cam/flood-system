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
                res.append((station.name,level))
    result = sorted_by_key(res,1)
    return result

def stations_highest_rel_level(stations,N):
    res = stations_level_over_threshold(stations,0)
    lst = []
    for i in range(0,N):
        lst.append(res[len(res)-i-1])
    return lst

        
