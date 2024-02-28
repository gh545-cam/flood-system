#Tests for Flood functions

from floodsystem.flood import *
from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():
    # Create Test Data
    stations = [
        MonitoringStation("Station 1", "Measurement 1", "Place 1", (0, 1), (0, 1), "River 1", "Town 1"),
        MonitoringStation("Station 2", "Measurement 2", "Place 2", (0, 2), (0, 1), "River 2", "Town 2"),
        MonitoringStation("Station 3", "Measurement 3", "Place 3", (0, 3), (1, 0), "River 3", "Town 3"),    # All typical ranges are consistent, bar station 3 , which is inconsistent.
        MonitoringStation("Station 4", "Measurement 4", "Place 4", (0, 4), (0, 1), "River 4", "Town 4"),
        MonitoringStation("Station 5", "Measurement 5", "Place 5", (0, 5), (0, 1), "River 5", "Town 5"),
        MonitoringStation("Station 6", "Measurement 6", "Place 6", (0, 6), (0, 1), "River 6", "Town 6"), 
    ] 

    stations[0].latest_level = 3
    stations[1].latest_level = None # Should be excluded - no data
    stations[2].latest_level = 4 # Should be excluded - inconsistent range
    stations[3].latest_level = 1
    stations[4].latest_level = -1 # Should be excluded - too low
    stations[5].latest_level = 2
    #Expected list: Station 1, Station 6, Station 4.
    list = stations_level_over_threshold(stations,0.8)
    test_list = []
    for (station,level) in list:
        test_list.append([station.station_id,level])
    assert test_list == [["Station 1",3],["Station 6",2],["Station 4",1]]
    list = stations_level_over_threshold(stations,1.2) #Higher Threshold
    test_list = []
    for (station,level) in list:
        test_list.append([station.station_id,level])
    assert test_list == [["Station 1",3],["Station 6",2]]

def test_stations_highest_rel_level():
    # Create Test Data
    stations = [
        MonitoringStation("Station 1", "Measurement 1", "Place 1", (0, 1), (0, 1), "River 1", "Town 1"),
        MonitoringStation("Station 2", "Measurement 2", "Place 2", (0, 2), (0, 1), "River 2", "Town 2"),
        MonitoringStation("Station 3", "Measurement 3", "Place 3", (0, 3), (1, 0), "River 3", "Town 3"),    # All typical ranges are consistent, bar station 3 , which is inconsistent.
        MonitoringStation("Station 4", "Measurement 4", "Place 4", (0, 4), (0, 1), "River 4", "Town 4"),
        MonitoringStation("Station 5", "Measurement 5", "Place 5", (0, 5), (0, 1), "River 5", "Town 5"),
        MonitoringStation("Station 6", "Measurement 6", "Place 6", (0, 6), (0, 1), "River 6", "Town 6"), 
    ] 
    stations[0].latest_level = 5
    stations[1].latest_level = None # Should be excluded - no data
    stations[2].latest_level = 4 # Should be excluded - inconsistent range
    stations[3].latest_level = 2
    stations[4].latest_level = -1 #Excluded as relative levels below 0 excluded.
    stations[5].latest_level = 3
    list = stations_highest_rel_level(stations,1) # Test for highest relative station
    test_list=[]
    for (station,level) in list:
        test_list.append([station.name,level])
    assert test_list == [["Place 1",5]]
    list = stations_highest_rel_level(stations,4) # Test for over full length, should result in 3 items (full list)
    test_list=[]
    for (station,level) in list:
        test_list.append([station.name,level])
    assert test_list == [["Place 1",5],["Place 6",3],["Place 4",2]]