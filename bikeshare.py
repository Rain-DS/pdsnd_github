import time
import pandas as pd
import numpy as np
from statistics import mode as md

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city would you love to analyze - chicago, new york city or washington:\n').lower()
    while city not in CITY_DATA:
        print('The city you entered does not exist, please try again...\n') 
        city = input('Which city would you love to analyze - chicago, new york city or washington:\n').lower()

    # Get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    print('\nSelect your month filter from any of the following months...')
    print('January, February, March, April, May, June, or all for no month filter')
    month = input('Enter your month filter here:\n').lower()
    
    # Adjust input until user inserts available month name
    while month not in months:
        month = input('\nThe month you entered is not available. Try again...\nEnter your month filter here:\n').lower()
    
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All']
    day = input('\nWhich day of the week would you like to filter by? Enter \'all\' for no day filter:\n').title()
    
    # Adjust input until user inserts recognized day name
    while day not in days:
        print('\nThe day you entered does not exist. Please try again...')
        day = input('\nWhich day of the week would you like to filter by? Enter \'all\' for no day filter:\n').title()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Read user-selected csv file
    df = pd.read_csv(CITY_DATA[city])
    
    # Extract pandas-readable start time, month, day of week, and hour data
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour
    
    # Filter df by user-specified month or leave as is if month equals all 
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    elif month == 'all':
        df = df
    
    # Filter df by user-specified day or leave as is if day equals all
    if day != 'All':
        df = df[df['day_of_week'] == day]
    elif day == 'All':
        df = df

    return df


def time_stats(df, month, day):
    """
    Displays statistics on the most frequent times of travel.
    
    Args:
        (dataframe) df - pre-filtered dataframe
        (str) month - selected name of month or "all" if none was selected
        (str) day - selected name of day or "all" if none was selected
    """

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # Display the most common month if no month filter was applied
    if month == 'all':
        most_freq_month = df['month'].mode()[0]
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_name = months[most_freq_month - 1].title()
        print('\nThe most frequent month of travel is:', month_name)
    else:
        print('\nCannot calculate most frequent month when dataset is filtered by just one month.')
        
    # Display the most common day of week if no day filter was applied
    if day == 'All':
        most_freq_day = df['day_of_week'].mode()[0]
        print('\nThe most frequent day of travel is:', most_freq_day)
    else:
        print('\nCannot calculate most frequent day when dataset is filtered by just one day.')

    # Display the most common start hour
    most_freq_hour = df['start_hour'].mode()[0]
    print('\nThe most frequent start hour is:', most_freq_hour)

    print("\nThis took %s seconds to calculate." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # Display most commonly used start station
    most_freq_start_stn = df['Start Station'].mode()[0]
    print('\nThe most commonly used start station is:', most_freq_start_stn)

    # Display most commonly used end station
    most_freq_end_stn = df['End Station'].mode()[0]
    print('\nThe most commonly used end station is:', most_freq_end_stn)

    # Display most frequent combination of start station and end station trip
    start_list = list(df['Start Station'])
    end_list = list(df['End Station'])
    combo_list = list(zip(start_list, end_list))
    print('\nThe most frequent combination of start station and end station is:', md(combo_list))

    print("\nThis took %s seconds." %(time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time in minutes
    print('Users spent a total travel time of %f minutes on the road.\n' %((df['Trip Duration'].sum())/60))

    # Display mean travel time in minutes
    print('On average, users spent %f minutes per travel.\n' %((df['Trip Duration'].mean())/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User type statistics:\n')
    print(df['User Type'].value_counts())

    # Use an 'if' condition to only display gender and birth stats if column is present in df
    if 'Gender' in df.columns:
        # Display counts of gender
        print('\nGender statistics:\n')
        print(df['Gender'].value_counts())

        # Display earliest, most recent, and most common year of birth
        print('\nBirth year statistics: ')
        print('\nThe earliest recorded birth year is:', int(df['Birth Year'].max()))
        print('\nThe most recent recorded birth year is:', int(df['Birth Year'].min()))
        print('\nMost common birth year is:', int(df['Birth Year'].mode()[0]))
    else:
        print('\nThere is no gender and birth year data to calculate.\n')
        pass
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def sample_data(df):
    """Returns the next 5 rows of data for as long as the user desires."""
    
    print('\nWould you like to see a sample of the first 5 items on the data set?')
    request = input('\nEnter \'yes\' to see, or \'no\' to skip: \n').lower()
    counter = 0
    # Use while loop to keep displaying next 5 raw data until user enters no
    while request == 'yes':
        print(df[counter:counter+5])
        counter += 5
        request = input('Would you like to see the next 5?\nEnter yes to see, or no to skip:\n').lower()
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        sample_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('\nProgram shutdown initiated...\nShutdown complete.')
            break


if __name__ == "__main__":
	main()
