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
    df['price'] = pd.to_numeric(df['price'].replace('[\$,]', '', regex=True), errors='coerce')
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

def most_expensive_neighbourhood(df):
    """
    Returns the neighbourhood with the highest average price.

    >>> most_expensive_neighbourhood(framing())
    'Fort Wadsworth'
    """
    df = exp_aps(df)
    mean_prices = df.groupby('neighbourhood')['price'].mean().sort_values(ascending=False)
    return mean_prices.idxmax()

def most_popular_lists_by_reviews(df):
    """
    Returns 5 listings with the most reviews.

    >>> most_popular_lists_by_reviews(framing())
    ['Room near JFK Queen Bed', 'Great Bedroom in Manhattan', 'Beautiful Bedroom in Manhattan', 'Private Bedroom in Manhattan', 'Room Near JFK Twin Beds']
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


def people_with_most_expencive_rooms():
    pass


def most_popular_names():
    pass


def unusable_rooms():
    pass


def identical_listings():
    pass


def price_of_avg_to_popular():
    pass


def similar_coordinates():
    pass


def avg_price_of_private_room():
    pass


def avg_price_of_apart_or_house():
    pass


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
