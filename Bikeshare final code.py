import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york city', 'washington']
MONTH_DATA = ['january', 'febraury', 'march', 'april', 'may', 'june','all']
DAY_DATA = ['monday', 'teusday', 'wednsday', 'thrusday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city_input = input('\nKindly enter a city to explore data: chicago, new york city or washington?\n')
        city = city_input.lower()
        try:
            if city in CITIES:
                break    
            else:
                print('Sorry, No data for this city!\nKindly choose from chicago, new york city or washington.')
        except ValueError and KeyboardInterrupt:
            print('Wrong input, please try again!')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month_input = input('\nKindly enter a month: january, febraury, march, april, may, june or all?\n')
        month = month_input.lower()
        try:
            if month in MONTH_DATA:
                break
            else:
                print('Sorry, No data for this month!\nKindly choose from january, febraury, march, april, may, june or all.') 
        except ValueError and KeyboardInterrupt:
            print('Wrong input please try again!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_input = input('\nKindly enter a day: monday, teusday, wednsday, thrusday, friday, saturday, sunday or all?\n')
        day = day_input.lower()
        try:
            if day.lower() in DAY_DATA:
                break
            else:
                print('sorry,no data for this day!\nKindly choose from monday, teusday, wednsday, thrusday, friday, saturday, sunday or all.')
        except ValueError and KeyboardInterrupt:
            print('Wrong input please try again!')

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
    df = pd.read_csv(CITY_DATA[city])
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

     # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nThe most common month is {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('\nThe most common day of week is {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('\nThe most common start hour is {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nThe most common start station is {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('\nThe most common end station is {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    start_end_combo = df.groupby(['Start Station','End Station'])
    print('\nThe most common start and end station comination is: ',start_end_combo.size().sort_values(ascending= False).head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = int(df['Trip Duration'].sum())
    days = total_time // 86400
    remainder_hours = total_time % 86400
    hours = remainder_hours // 3600
    remainder_seconds = remainder_hours % 3600
    minutes = remainder_seconds // 60
    seconds = remainder_seconds % 60
    print('\nThe total travel time is: {} seconds, equal to {} days, {} hours, {} minutes and {} seconds'.format( total_time, days, hours, minutes, seconds))

    # TO DO: display mean travel time
    print('\nThe average travel time is: {} seconds'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nThe counts of user types is: ', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('\nThe counts of user gender is: ', df['Gender'].value_counts())
        print('\The earliest year of birth is: ', df['Birth Year'].min())
        print('\The most recent year of birth is: ', df['Birth Year'].max())
        print('\The most common year of birth is: ', df['Birth Year'].mode())
    else:
        print('Sorry, no data about gender and birth year for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_show(df):
    """Display row data, 5 rows for every iteration."""

    print('\nShowing row data...\n')
    start_time = time.time()

    n = 0
    while True:
        print(df.iloc[n: n+5])
        while True:
            show_option = input('Would you like to show more data? yes or no')
            if show_option.lower() not in ['yes', 'no']:
                print('invalid input')
            else:
                break
        if show_option == 'yes':
            n += 5
        else:
            break
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        data_show(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
