import matplotlib
import numpy as np


def polyfit(dates, levels, p):
    date_float = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(date_float-date_float[0], levels, p)
    poly = np.poly1d(p_coeff)
    return poly, date_float[0]

