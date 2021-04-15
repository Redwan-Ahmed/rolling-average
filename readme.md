## Rolling Averages

# Functions I created:
* I created my own function (rolling_avg function), that converts the csv file into a data frame (using the pandas library). I then calculated the 'Rolling Average Value' using the rolling method (`f['value'].rolling(window=600).mean()`), I assumed the window size that is 600s. Lastly, I used the matplotlib.pyplot library to plot the line graph (`df.plot.line(x='time', y=['value', 'Rolling Average Value'])`).
* Inside the calculate_rolling_average function, I converted the "input_array" that is passed in through the parameter into a data series using pandas. Once converted I perfomed the rolling method using pandas, I also converted the series back into a list so that you can see each inividual average (you will need to remove the comment section to print the list (line 72) due to the length of the output). In addition, I included a Max Value which returns the highest value in the average list.

# Libraries used in this project?
* Note: You will need both libraries installed for the code to run. Use pip for easy installation.
1. pandas 
2. matplotlib.pyplot

# How to run the soloution:
1. Simply run the python code in the terminal.
2. A new window will appear displaying the line graph.

# Images(attached):
* **Rolling Average Line Graph.png** - this is the line graph that is generated. (rolling_avg function)
* **Terminal Output - DataFrame.png** - this displays all the data in the CSV including a new column called "Rolling Average Value". (rolling_avg function)
* **Terminal Output - Max Value.png** - this displays the maximum value in the rolling average value. (calculate_rolling_average function)
* **Terminal Output - Rolling Avg List.png** - this displays the data series of the rolling average value. (calculate_rolling_average function)
