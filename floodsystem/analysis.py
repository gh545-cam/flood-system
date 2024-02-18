import matplotlib
import numpy as np


def polyfit(dates, levels, p):
    #performs polynomial fitting to water level against date data for particular station
    date_float = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(date_float-date_float[0], levels, p)
    #shifts date by date_float[0] to prevent inaccuracy with large numbers and memory overflow
    poly = np.poly1d(p_coeff)
    return poly, date_float[0]

