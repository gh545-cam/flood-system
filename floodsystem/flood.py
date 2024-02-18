from . import datafetcher
from .station import MonitoringStation
from .utils import sorted_by_key


def stations_level_over_threshold(stations,tol):
    #iterates through stations to find station objects with relative water level greater than input tolerance
    res = []
    for station in stations:
        bol = station.typical_range_consistent()
        #check range consistency, if not consistent ignore particular station
        if bol == True:
            level = station.relative_water_level()
            #calculate relative water level by method
            if level != None and level > tol:
                res.append((station,level))
    result = sorted_by_key(res,1)
    #sort by water level
    return result

def stations_highest_rel_level(stations,N):
    #returns top N stations with highest water level in descending order
    res = stations_level_over_threshold(stations,0)
    lst = []
    i = len(lst)
    while len(lst) < N:
        s = res[len(res) - 1 - len(lst)][0]
        lst.append((s,res[len(res)-1-len(lst)][1]))
    return lst

        
