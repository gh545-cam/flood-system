# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
from .utils import sorted_by_key

def stations_by_distance(stations,p):
    res = []
    for s in stations:
        c = s.coord
        distance = haversine(c,p)
        res.append((s,distance))
    result = sorted_by_key(res,1)
    return result

def stations_within_radius(stations, centre, r):
    res = []
    for s in stations:
        c = s.coord
        distance = haversine(c,centre)
        if distance <= r:
            res.append(s)
    return res

def rivers_with_station(stations):
    res = []
    for s in stations:
        riv = s.river
        res.append(riv)
    result = set(res)
    return result

def stations_by_river(stations):
    dic = {}
    for s in stations:
        riv = s.river
        if riv not in dic.keys():
            dic[riv] = [s]
        else:
            dic[riv].append(s)
    return dic