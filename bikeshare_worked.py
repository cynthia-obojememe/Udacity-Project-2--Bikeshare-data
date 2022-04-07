import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv', }

MONTH_DATA = {'january': 1,
              'february': 2,
              'march': 3,
              'april': 4,
              'may': 5,
              'june': 6,
              'all': 'all', }

DAYS_LIST = {'all': 'all', 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6,
             'sunday': 7}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    # """

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # def city_info():

    """
        Asks user to specify a city, month, and day to analyze.
    """

    print('Hello! I am happy to help you. Let\'s explore some US bikeshare data!')
#     city_datas = ('chicago',
#                   'new york city',
#                   'washington')

    while True:
        city = (input(
            "\nPlease input a City which you would like to analyse? Choose from chicago, new york city or washington\n:")).lower()
        if city in CITY_DATA:

            print(" Good to Go!")
            break
        else:
            print("you have entered a wrong input, Do not stop my program, Please try again!.")

    # get user input for month (all, january, february, ... , june)

    # Creating a dictionary similar to CITY_DATA to store each month to and 'all' option

    while True:
        month = str(input("\nPlease enter the month, between January to June, for which you're seeking the data, "
                          "please type 'all' to view all months data.:\n")).lower()

        if month in MONTH_DATA:
            print(f"\nYou have chosen {month.title()} as your month.")
            break
        print("Please try again and input the accepted format.(spell month in full)")

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = str(input("\nPlease enter your preferred day of the week,(e.g, monday)"
                        "please type 'all' or view all option.:\n")).lower()
        print(f"\nYou have chosen {day.title()} as your days_of_week.")
        if day in DAYS_LIST:
            break
        print("Please try again and input the accepted format for the day of the week:")

    print('-' * 40)
    return city, month, day


# city, month, day = get_filters()

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
    # Load data for city
    df = pd.read_csv(CITY_DATA[city])

    # convert start time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract year, from Start Time to create new columns
    df['year'] = df['Start Time'].dt.year

    # extract month from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    # extract month from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.day_of_week

    # extract month from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour

    # filter month by user input:
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH_DATA.get(month)

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    #     filter by day of week if applicable

    if day != 'all':
        day = DAYS_LIST.get(day)
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day]

    return df


# load_data(city, month, day)


def time_stats(df):
    # Convert the Start Time column to datetime and check datatype

    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    most_common_month = df['month'].mode()[0]
    print("The most common month from the given filtered data is: "+ str (most_common_month))

    # display the most common day of week

    most_common_day = df['day_of_week'].mode()[0]

    print("The most common day of week from the given data is : "+ str (most_common_day))

    # display the most common start hour

    most_common_start_hour = df['hour'].mode()[0]
    print(f"The most common start hour from the given filtered data is:" + str(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


# time_stats(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: " + most_common_end_station)

    # display most frequent combination of start station and end station trip

    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(
        frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time from the given fitered data is: " + str(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time from the given fitered data is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()[0]
    print("\nThe count of user types are: \n" + str(user_types))

    # Display counts of gender
    gender = df['Gender'].value_counts()[0]
    print("\nThe count of user gender are \n" + str(gender))

    # Display earliest, most recent, and most common year of birth

    earliest_birth = df['Birth Year'].min()
    most_recent_birth = df['Birth Year'].max()
    most_common_birth = df['Birth Year'].mode()
    print('Earliest birth from the given filtered data is: {}\n'.format(earliest_birth))
    print('Most recent birth from the given filtered data is: {}\n'.format(most_recent_birth))
    print('Most common birth from the given filtered data is: {}\n'.format(most_common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def view_raw_data(df):
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next + 5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_raw_data(df)


if __name__ == "__main__":
    main()
