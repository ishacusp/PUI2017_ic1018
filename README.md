Homework 2 : https://github.com/ishacusp/PUI2017_ic1018/

Assignment 1:
I created show_bus_locations_ic1018.py file which takes MTA_KEY and BUS_LINE as command line inputs to fetch the JSON file from the url
address. I then load the JSON file and store it into 'data' as a pandas data frame. Later I print the count number of active buses and
print out the locations of these buses. To see the output, one has to pass the given file name, MTA_KEY and BUS_LINE as command line 
arguments.
I took help from Gaurav to know the location of the bus location' coordinates in the 'data' dataframe. To make the 'data' dataframe easy to read,
I created a dummy JSON file and transfered all the contents of 'data' in it. Later I opened the dummy JSON file in a JSON reader to
easily read the contents of the JSON file. This helped me to carry out further tasks in the Homework 2 quite easily.

Assignment 2:
I repeated the same process here as in Assignment 1. I created a get_bus_info_ic1018.py which requires user to enter 4 command line inputs:
the given python file name, MTA_KEY, BUS_LINE, and the BUS_LINE csv file. Here the python file loads the JSON file and stores the file into
'data' as a pandas data frame. It then writes the information about the bus lines' next stops in the given csv file.

Assignment 3:
In this assignment, I took the NYC Demographic statistics broken by school districts data stored as a csv file from the urban profiler 
(http://urbanprofiler.cloudapp.net/dataset/g3vh-kbnw/). I read the file and stored it as a dataframe to perform given tasks in the assignment.
I took help from Ben Steers to perform the task : 'remove all the numberical columns except the 'PERCENT FEMALE' & 'PERCENT MALE' column'.

Extra Credit:
I repeated the same process here as in Assignment 3. I took the 2001 City Office Election Campaign expenditures data from the 
urban profiler (http://urbanprofiler.cloudapp.net/dataset/k3cd-yu9d/). I did this assignment on my own.

 
