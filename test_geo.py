#tests for geo functions

from floodsystem.geo import *
from floodsystem.station import MonitoringStation


def test_stations_by_distance():

    # Create 1st station
    s1 = MonitoringStation(station_id="test-s-id-1",
                          measure_id="test-m-id-1",
                          label="Station 1",
                          coord=(-2.0, 4.0),
                          typical_range=(-2.3, 3.4445),
                          river="River X",
                          town="My Town"
                          )
    
        # Create 1st station
    s2 = MonitoringStation(station_id="test-s-id-2",
                          measure_id="test-m-id-2",
                          label="Station 2",
                          coord=(-7.0, 3.0),
                          typical_range=(-2.3, 3.4445),
                          river="River X",
                          town="My Town"
                          )

    stations = [s1,s2]

    # Create a coordinate p
    p = (52.2053, 0.1218)

    result = stations_by_distance(stations, p)

    assert result == [(s1, 6038.3717730613525), (s2, 6589.027461288413)]


def test_stations_within_radius():
    # Create mock data
    s1=MonitoringStation(station_id="test-s-id-1",
                          measure_id="test-m-id-1",
                          label="Trumptington",
                          coord=((53.2053, 0.1418)),
                          typical_range=(-2.3, 3.4445),
                          river="River X",
                          town="My Town"
                          )
    
    s2 = MonitoringStation(station_id="test-s-id-2",
                          measure_id="test-m-id-2",
                          label="London",
                          coord=(51.5074, -0.1278),
                          typical_range=(-2.3, 3.4445),
                          river="River X",
                          town="My Town"
                          )
    
    s3 = MonitoringStation(station_id="test-s-id-3",
                          measure_id="test-m-id-3",
                          label="Station 3",
                          coord=(52.4862, -1.8904),
                          typical_range=(-2.3, 3.4445),
                          river="River X",
                          town="My Town"
                          )

    stations = [s1,s2,s3]

    # Define a center point and radius
    center = (52.2053, 0.1218) # Cambridge location
    radius = 90

    # Call the function
    nearby_stations = stations_within_radius(stations, center, radius)

    # Check if the function returns only the stations within the radius
    assert len(nearby_stations) == 1
    assert nearby_stations[0].name== "London"

def test_rivers_with_station():
    # Create mock data
    stations = [
        MonitoringStation("id1", "measure1", "Station1", (0, 0), (0, 1), "River Thames", "Town1"),
        MonitoringStation("id2", "measure2", "Station2", (1, 1), (1, 2), "River Cam", "Town2"),
        MonitoringStation("id3", "measure3", "Station3", (2, 2), (2, 3), "River Thames", "Town3")
    ]

    # Expected result
    expected_rivers = {"River Thames", "River Cam"}

    # Call the function
    result = rivers_with_station(stations)

    # Assert the result
    assert result == expected_rivers, "The function should return the correct set of river names."

def test_stations_by_river():
    # Create mock data
    stations = [
        MonitoringStation("id1", "measure1", "Station1", (0, 0), (0, 1), "River Thames", "Town1"),
        MonitoringStation("id2", "measure2", "Station2", (1, 1), (1, 2), "River Cam", "Town2"),
        MonitoringStation("id3", "measure3", "Station3", (2, 2), (2, 3), "River Thames", "Town3")
    ]

    # Expected result
    expected_dict = {
        "River Thames": ["Station1", "Station3"],
        "River Cam": ["Station2"]
    }

    # Call the function
    river_dict = stations_by_river(stations)

    # Assert the result
    assert river_dict == expected_dict, "The function should return the correct mapping of rivers to station names."

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