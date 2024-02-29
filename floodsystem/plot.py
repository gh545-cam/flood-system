import matplotlib.pyplot as plt 
from datetime import datetime, timedelta
from .datafetcher import fetch_measure_levels
from .analysis import polyfit
import matplotlib
import numpy as np

def plot_water_levels(station,dates,levels):
    #plots water level against time for particular station
    f, = plt.plot(dates,levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.axhline(y = station.typical_range[0])
    plt.axhline(y = station.typical_range[1])
    plt.tight_layout()
    plt.show()
    dateslist = f.get_xdata()
    levelslist = f.get_ydata()
    return dateslist,levelslist

def plot_water_level_with_fit(station, dates, levels, p):
    #plots actual and polynomial fitted water level against time for particular station
    f, = plt.plot(dates,levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.axhline(y = station.typical_range[0])
    plt.axhline(y = station.typical_range[1])
    plt.tight_layout()
    poly, d0 = polyfit(dates, levels, p)
    #create polynomial fit and plot
    x1 = np.linspace(matplotlib.dates.date2num(dates)[0], matplotlib.dates.date2num(dates)[-1], 30)
    plt.plot(x1, poly(x1 - d0))
    plt.show()
    dateslist = f.get_xdata()
    levelslist = f.get_ydata()
    return dateslist,levelslist