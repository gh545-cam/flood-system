import matplotlib.pyplot as plt 
from datetime import datetime, timedelta
from .datafetcher import fetch_measure_levels
from .analysis import polyfit
import matplotlib
import numpy as np

def plot_water_levels(station,dates,levels):
    plt.plot(dates,levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    plt.plot(matplotlib.dates.date2num(dates),levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    poly, d0 = polyfit(dates, levels, p)
    x1 = np.linspace(matplotlib.dates.date2num(dates)[0], matplotlib.dates.date2num(dates)[-1], 30)
    plt.plot(x1, poly(x1 - d0))
    plt.show()