import csv
import pandas as pd
import matplotlib.pyplot as plt

''' example.csv contains the values for the system. The thing to note about the file
    is that the sampling periods are not every 1 second. So there might be a value at 
    t = 0s of 200, and then the next value at t = 3s of 210 watts. We can assume that
    the power value for times 1s, and 2s are also 200 watts. (So the power profile is a step
    function)

    Example call
    ===========
    time_array, input_array = load_csv()
    max_value, rolling_times, rolling_avg = calculate_rolling_average(time_array, input_array, averaging_period=600)

'''

def rolling_avg():
    """ This is my own function that calculates a rolling average and displays the results in a line graph.
        1) example.csv is extracted using Pandas and converted into a DataFrame (df).
        2) 'Rolling Average Value' is calculated using Pandas Rolling method, the window size is 600s.
        3) df.plot.line - using the matplotlib.pyplot library I plotted the line graph. 
        3.1) Note: the X axis is 'time' and the Y axis are the 'value' and 'rolling avg value'.
        4) plt.show() - this displays the line graph.
    """
    df = pd.read_csv('example.csv')
    df['Rolling Average Value'] = df['value'].rolling(window=600).mean()
    print("DataFrame \n", df)
    df.plot.line(x='time', y=['value', 'Rolling Average Value'])
    plt.show()

def load_csv():
    """ load the CSV containing the values.

    Returns:
        tuple: first element sampling points, second element power values

    """
    time_array = []
    input_array = []
    with open('example.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(reader):
            if index > 0:
                time_array.append(int(float(row[1])))
                input_array.append(int(float(row[2])))

    return time_array, input_array

def calculate_rolling_average(time_array, input_array, averaging_period=600):
    """Summary
    Calculate a rolling average

    Args:
        time_array (list): sampling points
        input_array (list): power values
        averaging_period (int): (optional) default 10 minutes (600s)

    Returns:
        tuple: Max value, sampled times, and sampled value
    """
    # converted the list into a pandas data series.
    input_array_series = pd.Series(input_array)
    # using pandas I calculated the rolling average. 
    input_array_average = input_array_series.rolling(window=averaging_period).mean()
    # converted the data series back to a list 
    input_array_average_list = input_array_average.tolist()
    # calculated the maximum value using Pandas  
    max_value = input_array_average.max()

    print("Rolling Average \n", input_array_average)
    # "remove comment to print the entire list" print("Rolling Average \n", input_array_average_list)
    print("Max Value", max_value)

    return max_value, time_array, input_array_average_list

# calling the csv function.
time_array, input_array = load_csv()
# calling the calculate_rolling_average function.
calculate_rolling_average(time_array, input_array, 600)
# calling the rolling_avg function.
rolling_avg()
