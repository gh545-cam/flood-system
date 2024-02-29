from floodsystem.analysis import *
import matplotlib
import matplotlib.dates
import numpy as np

#Create test functions to create data
def function1(x):
    return x**2 + 3*x

def function2(x):
    return x**3 + 4*(x**2)+7*x

def function3(x):
    return 2*(x**4) + 3*x + 5

def test_polyfit():
    test_array1 = []
    test_array2 = []
    test_array3 = []
    x = []
    for i in range(1,51):
        x.append(i)
        test_array1.append(function1(i))
        test_array2.append(function2(i))
        test_array3.append(function3(i))
    x_dates = matplotlib.dates.num2date(x)

    #pass values through function
    polynomial1,placeholder = polyfit(x_dates,test_array1,2)
    polynomial2,placeholder = polyfit(x_dates,test_array2,3)
    polynomial3,placeholder = polyfit(x_dates,test_array3,4)
    #Calculate Predicted values for the function.
    value1 = polynomial1(100)
    value2 = polynomial2(100)
    value3 = polynomial3(100)
    #Calculate expected values from test function
    expected_value1 = function1(100) 
    expected_value2 = function2(100)
    expected_value3 = function3(100)
    #Polyfit is only able to approximate the function's value -> 5% or better relative accuracy is considered acceptable.
    rel_error1 = abs((value1-expected_value1)/expected_value1)
    rel_error2 = abs((value2-expected_value2)/expected_value2)
    rel_error3 = abs((value3-expected_value3)/expected_value3)
    assert rel_error1 < 0.05
    assert rel_error2 < 0.05
    assert rel_error3 < 0.05
    
