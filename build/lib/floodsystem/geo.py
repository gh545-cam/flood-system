# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
from .utils import sorted_by_key

def stations_by_distance(stations,p):
    #creates list of station objects and corresponding distance ordered by distance to given coordinate p using haversine function with list of station objects (stations) as input.
    res = []
    for s in stations:
        c = s.coord
        #retrieves coordinate for station s
        distance = haversine(c,p)
        #calculates distance using haversine
        res.append((s,distance))
        #appends station and corresponding distance to result list.
    result = sorted_by_key(res,1)
    #order by distance
    return result

def stations_within_radius(stations, centre, r):
    #returns list of all station objects within a distance r km away from input center coordinates with list of station objects as input.
    res = []
    for s in stations:
        c = s.coord
        #retrieves coordinate for station s
        distance = haversine(c,centre)
        if distance <= r:
            res.append(s)
            #appends station to list if distance to center is within radius r
    return res

def rivers_with_station(stations):
    #compiles set of rivers with one or more stations from a list of station objects.
    res = []
    for s in stations:
        riv = s.river
        res.append(riv)
    result = set(res)
    return result

def stations_by_river(stations):
    #returns dicitionary of rivers as key and list of station objects located at that river as values.
    dic = {}
    for s in stations:
        riv = s.river
        if riv not in dic.keys():
            dic[riv] = [s]
        else:
            dic[riv].append(s)
    return dic

def rivers_by_station_number(stations, N):
    #reteurns first N rivers with the highest station numbers
    dic = {}
    for s in stations:
        #iterates through stations to create dictionary of number of stations each river has with river as key and count as value
        riv = s.river
        if riv not in dic.keys():
            dic[riv] = 1
        else:
            dic[riv] +=1
    lst = []
    for key in dic.keys():
        #creates list of (river, station count) tuples in list lst
        lst.append((key,dic[key]))
    lst = sorted_by_key(lst,1,True)
    #sorts lst by decreasing number of stations
    res = lst[:N]
    #takes the first N rivers
    for i in range(N,len(lst)):
        #checks to see if other rivers have the same number of stations as the last river in res, if so append to res
        last = res[-1][1] 
        num = lst[i][1]
        if last == num:
            res.append(lst[i])
        elif last < num:
            break
    return res