### Date created
11/25/2019

### Project Title
Explore US Bikeshare Data 

### Project Description
The Explore US Bikeshare project uses Python to explore data related to bike share systems for three major cities in the United States — Chicago, New York City, and Washington. The program imports wrangled raw data from existing .csv files hidden away in .gitignore and answers interesting questions about it by computing descriptive statistics. It is built to be interactive so users can explore data for any city, month or day, as they so choose. Results are presented in the terminal.

### Files used
The project uses wrangled data stored in the following files:
- chicago.csv
- new_york_city.csv
- washington.csv 

You can access raw data used for the project [here](https://www.capitalbikeshare.com/system-data).

For data wrangling purposes, note that the core data that forms the base of this experiment includes the following columns in all 3 city files:
- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year

Also note that data for the project was randomly selected from the first 6 months of 2017 for all three cities. Feel free to use as much data as you desire to test run the project on your terminal.

### Contribution
For now, the project only calculates data relating to the following broad questions:
- Popular times of travel (i.e., occurs most often in the start time)
- Popular stations and trip
- Trip duration
- User info

Feel free to expand upon the solutions provided by the project through your contributions. If your desired contribution provides solutions to a broad new section, define your overall solution in a function and add it to the main function. If you are simply answering more questions within an existing broad section, include your code in the function defined for that broad question/section.

### Credits
Udacity Python for Data Science Nanodegree Program

