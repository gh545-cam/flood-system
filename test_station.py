# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    # Create Test Data
    s1=MonitoringStation(station_id="Station1",
                          measure_id="Measurement1",
                          label="Place1",
                          coord=((53.2053, 0.1418)),
                          typical_range=(5,-2.3), #Incorrect Order
                          river="River1",
                          town="Town1")
    s2=MonitoringStation(station_id="Station2",
                          measure_id="Measurement2",
                          label="Place2",
                          coord=((53.2053, 0.1418)),
                          typical_range=(), #Nonexistent data
                          river="River2",
                          town="Town2")
    s3=MonitoringStation(station_id="Station3",
                          measure_id="Measurement3",
                          label="Place3",
                          coord=((53.2053, 0.1418)),
                          typical_range=(-2.3,5), #Accurate
                          river="River3",
                          town="Town3")
    s4=MonitoringStation(station_id="Station4",
                          measure_id="Measurement4",
                          label="Place4",
                          coord=((53.2053, 0.1418)),
                          typical_range=(-2.3,5), #Equal is considered as accurate
                          river="River4",
                          town="Town4")
    
    assert s1.typical_range_consistent() == False
    assert s2.typical_range_consistent() == False
    assert s3.typical_range_consistent() == True
    assert s4.typical_range_consistent() == True

def test_inconsistent_typical_range_stations():
    # Create Test Data
    stations = [
        MonitoringStation("Station 1", "Measurement 1", "Place 1", (0, 1), (0, 1), "River 1", "Town 1"),
        MonitoringStation("Station 2", "Measurement 2", "Place 2", (0, 2), (0, 1), "River 2", "Town 2"),
        MonitoringStation("Station 3", "Measurement 3", "Place 3", (0, 3), (0, 1), "River 3", "Town 3"),
        MonitoringStation("Station 4", "Measurement 4", "Place 4", (0, 4), (0, 1), "River 4", "Town 4"),
        MonitoringStation("Station 5", "Measurement 5", "Place 5", (0, 5), (0, 1), "River 5", "Town 5"),  # All data is consistent
    ]

    assert inconsistent_typical_range_stations(stations) == []

    #Replace Test Data
    stations2 = [
        MonitoringStation("Station 6", "Measurement 6", "Place 6", (0, 6), (1, 1), "River 6", "Town 6"), # Equal is considered accurate
        MonitoringStation("Station 7", "Measurement 7", "Place 7", (0, 7), (0, 1), "River 7", "Town 7"), # Accurate
        MonitoringStation("Station 8", "Measurement 8", "Place 8", (0, 8), (2, 1), "River 8", "Town 8"), # Wrong order
        MonitoringStation("Station 9", "Measurement 9", "Place 9", (0, 9), (), "River 9", "Town 9"), # Non-existent
    ]

    inconsistent_station_list = inconsistent_typical_range_stations(stations2)
    #print(inconsistent_station_list)
    assert inconsistent_station_list == ["Place 8", "Place 9"]

test_inconsistent_typical_range_stations()