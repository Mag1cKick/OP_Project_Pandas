"""pandas project"""
import pandas as pd

def framing():
    """creates pandas DataFrame"""
    file = 'train.csv'
    df = pd.read_csv(file)
    return df

def exp_aps(df):
    """sorts prices
    #>>> exp_aps(framing())
    """
    df['price'] = pd.to_numeric(df['price'].replace(r'[\$,]', '', regex=True), errors='coerce')
    sorted_df = df.sort_values(by='price', ascending=False)
    return sorted_df

def most_expensive_neighborhood_group(frame):
    """
    Returns the neighborhood_group with the highest average price.

    >>> most_expensive_neighborhood_group(framing())
    'Manhattan'
    """
    df = exp_aps(frame)
    mean_prices = df.groupby('neighbourhood_group')['price'].mean().sort_values(ascending=False)
    return mean_prices.idxmax()

def most_expensive_neighbourhood(frame):
    """
    Returns the neighbourhood with the highest average price.

    >>> most_expensive_neighbourhood(framing())
    'Fort Wadsworth'
    """
    df = exp_aps(frame)
    mean_prices = df.groupby('neighbourhood')['price'].mean().sort_values(ascending=False)
    return mean_prices.idxmax()

def most_popular_lists_by_reviews(df):
    """
    Returns 5 listings with the most reviews.

    >>> most_popular_lists_by_reviews(framing())
    ['Room near JFK Queen Bed', 'Great Bedroom in Manhattan',\
 'Beautiful Bedroom in Manhattan', 'Private Bedroom in Manhattan', 'Room Near JFK Twin Beds']
    """
    df['number_of_reviews'] = pd.to_numeric(df['number_of_reviews'], errors='coerce')
    sorted_df = df.sort_values(by='number_of_reviews', ascending=False)
    return sorted_df.iloc[:5]['name'].tolist()

def most_popular_neighbourhood_group(df):
    """
    Returns the most popular neighborhood group based on the number of listings.

    >>> most_popular_neighbourhood_group(framing())
    'Manhattan'
    """
    counts = df['neighbourhood_group'].value_counts()
    return counts.idxmax()


def most_popular_neighbourhoods(df):
    """
    Returns the most popular neighborhoods based on the number of listings.

    >>> most_popular_neighbourhoods(framing())
    ['Williamsburg', 'Bedford-Stuyvesant', 'Harlem', 'Bushwick', 'Upper West Side']
    """
    counts = df['neighbourhood'].value_counts()
    return counts.index[:5].tolist()


def host_with_most_listings(df):
    """
    Returns the host with the most listings.

    >>> host_with_most_listings(framing())
    'Michael'
    """
    counts = df['host_name'].value_counts()
    return counts.idxmax()


def hosts_with_most_expensive_rooms(frame):
    """
    Returns the host with the most expensive room.

    >>> hosts_with_most_expensive_rooms(framing())
    'Kathrine'
    """
    df = exp_aps(frame)
    sorted_df = df.sort_values(by='price', ascending=False)
    return sorted_df.iloc[0]['host_name']

def most_popular_host(df):
    """
    Returns the host whose listings have the most total reviews.

    >>> most_popular_host(framing())
    'Michael'
    """
    df['number_of_reviews'] = pd.to_numeric(df['number_of_reviews'], errors='coerce')
    total_reviews = df.groupby('host_name')['number_of_reviews'].sum()
    return total_reviews.idxmax()


def unusable_rooms(df):
    """
    Returns all rooms that have 0 available days in year

    #>>> unusable_rooms(framing())
    """
    no_availability = df[df['availability_365'] == 0]
    return no_availability['name']


def price_of_avg_to_popular(frame):
    """
    Returns the ratio of the average price of 'Entire home/apt' to 'Private room'.

    >>> price_of_avg_to_popular(framing())
    2.36
    """
    df = exp_aps(frame)
    entire_home_avg = df[df['room_type'] == 'Entire home/apt']['price'].mean()
    private_room_avg = df[df['room_type'] == 'Private room']['price'].mean()
    return round(entire_home_avg / private_room_avg, 2)


def similar_coordinates(df):
    """
    Returns the names of all listings that have similar coordinates.

    #>>> similar_coordinates(framing())
    """
    duplicates = df[df.duplicated(subset=['latitude', 'longitude'], keep=False)]
    return duplicates['name']


def avg_price_of_private_room(frame):
    """
    Returns the average price of listings where the room type is 'Private room'.

    >>> avg_price_of_private_room(framing())
    89.78
    """
    df = exp_aps(frame)

    private_rooms = df[df['room_type'] == 'Private room']
    return round(private_rooms['price'].mean(), 2)


def avg_price_of_apart_or_house(frame):
    """
    Returns the average price of listings where the room type is 'Entire home/apt'.

    >>> avg_price_of_apart_or_house(framing())
    211.79
    """
    df = exp_aps(frame)
    entire_home = df[df['room_type'] == 'Entire home/apt']
    return round(entire_home['price'].mean(), 2)

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
