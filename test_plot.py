from floodsystem.station import MonitoringStation
from floodsystem.plot import *
from floodsystem.analysis import polyfit
import matplotlib
import pytest as py
import numpy as np

def test_plot_water_levels(): #This is to test that the plot object recieves the correct data when fed into the function. It is assumed that, given the correct data, the graph will be plotted correctly.
    #Create Test Station
    station = MonitoringStation("Station 1", "Measurement 1", "Place 1", (0, 1), (0, 1), "River 1", "Town 1")
    #Create Test Data
    dates = [0,1,2,3,4,5]
    levels = [1,2,3,4,5,6]
    datesplotted,levelsplotted = plot_water_levels(station,dates,levels)
    np.testing.assert_array_equal(datesplotted,dates)
    np.testing.assert_array_equal(levelsplotted,levels)

def test_plot_water_level_with_fit(): # Similar testing. Testing on the function fitting itself is in test_analysis.
    #Create Test Station
    station = MonitoringStation("Station 1", "Measurement 1", "Place 1", (0, 1), (0, 1), "River 1", "Town 1")
    #Create Test Data
    dates = [0,1,2,3,4,5]
    levels = [1,2,3,4,5,6]
    datesplotted,levelsplotted = plot_water_level_with_fit(station,dates,levels,4) #polynomial of 4 used in standard use.
    np.testing.assert_array_equal(datesplotted,dates)
    np.testing.assert_array_equal(levelsplotted,levels)