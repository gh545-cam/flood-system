#tests for geo functions

from floodsystem.geo import *
from floodsystem.station import MonitoringStation


def test_stations_by_distance():

    # Create station 1
    s1 = MonitoringStation(station_id="sta1", measure_id="m1",
                          label="Station1",
                          coord=(-2.0, 4.0),
                          typical_range=(-2.3, 3.4445),
                          river="r1",
                          town="t1"
                          )
    # Create 1st station
    s2 = MonitoringStation(station_id="sta2",
                          measure_id="m2",
                          label="Station2",
                          coord=(-7.0, 3.0),
                          typical_range=(-2.3, 3.4445),
                          river="r2",
                          town="t2"
                          )
    stations = [s1,s2]
    #create list of station objects stations
    # define random coordinate p
    p = (52.2053, 0.1218)
    result = stations_by_distance(stations, p)
    assert result == [(s1, 6038.3717730613525), (s2, 6589.027461288413)]
    #test that distance is correct + ordered in ascending order


def test_stations_within_radius():
    # Create mock data
    s1=MonitoringStation(station_id="sta1",
                          measure_id="m1",
                          label="Trumptington",
                          coord=((53.2053, 0.1418)),
                          typical_range=(-2.3, 3.4445),
                          river="r1",
                          town="t1"
                          )
    
    s2 = MonitoringStation(station_id="sta2",
                          measure_id="m2",
                          label="Cambridge",
                          coord=(51.5074, -0.1278),
                          typical_range=(-2.3, 3.4445),
                          river="r2",
                          town="t2"
                          )
    
    s3 = MonitoringStation(station_id="sta3",
                          measure_id="m3",
                          label="York",
                          coord=(52.4862, -1.8904),
                          typical_range=(-2.3, 3.4445),
                          river="r3",
                          town="t3"
                          )

    stations = [s1,s2,s3]

    # Create an aribitary center  and radius
    center = (52.2053, 0.1218) # Cambridge location
    radius = 90
    nearby_stations = stations_within_radius(stations, center, radius)

    # Check if the function returns only the stations within the radius
    assert len(nearby_stations) == 1
    assert nearby_stations[0].name== "Cambridge"

def test_rivers_with_station():
    # Create mock data
    stations = [
        MonitoringStation("id1", "m1", "S1", (0, 0), (0, 1), "River Thames", "t1"),
        MonitoringStation("id2", "m2", "S2", (1, 1), (1, 2), "River Cam", "t2"),
        MonitoringStation("id3", "m3", "S3", (2, 2), (2, 3), "River Thames", "t3")
    ]
    # Expected result
    expected_rivers = {"River Thames", "River Cam"}

    # Function result
    result = rivers_with_station(stations)

    # Compare the result
    assert result == expected_rivers, "the function returns the correct river names."

def test_stations_by_river():
    # Create mock data
    stations = [
        MonitoringStation("id1", "m1", "S1", (0, 0), (0, 1), "River Thames", "t1"),
        MonitoringStation("id2", "m2", "S2", (1, 1), (1, 2), "River Cam", "t2"),
        MonitoringStation("id3", "m3", "S3", (2, 2), (2, 3), "River Thames", "t3")
    ]

    expected_dict = {
        "River Thames": ["S1", "S3"],
        "River Cam": ["S2"]
    }

    # Function result
    river_dict = stations_by_river(stations)

    # Compare  result
    assert river_dict == expected_dict, "The function returns the correct results."

def test_rivers_by_station_number():
    # Create mock data
    stations = [
        MonitoringStation("id1", "measure1", "Station1", (0, 0), (0, 1), "River Thames", "Town1"),
        MonitoringStation("id2", "measure2", "Station2", (1, 1), (1, 2), "River Cam", "Town2"),
        MonitoringStation("id3", "measure3", "Station3", (2, 2), (2, 3), "River Thames", "Town3"),
        MonitoringStation("id4", "measure4", "Station4", (2, 2), (2, 3), "River Thames", "Town4"),
        MonitoringStation("id5", "measure5", "Station5", (3, 3), (3, 4), "River Avon", "Town5"),
        MonitoringStation("id6", "measure6", "Station6", (4, 4), (4, 5), "River Avon", "Town6"),
        MonitoringStation("id7", "measure7", "Station7", (3, 3), (3, 4), "River Blon", "Town7"),
        MonitoringStation("id8", "measure8", "Station8", (4, 4), (4, 5), "River Blon", "Town8")
    ]

    # Call the function
    result = rivers_by_station_number(stations, 2)

    # Assert the result
    assert (result == [("River Thames", 3), ("River Avon", 2),("River Blon", 2)] or
        result == [("River Thames", 3), ("River Blon", 2),("River Avon", 2)]), \
        "The function should return the correct list of top N rivers by station count."