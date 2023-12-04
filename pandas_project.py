"""pandas project"""
import pandas as pd

def framing():
    """creates pandas DataFrame"""
    file = '/Users/bohdanpopov/Documents/GitHub/OP_Project_Pandas/train.csv'
    df = pd.read_csv(file)
    return df

def exp_aps(df):
    """sorts prices"""
    df['price'] = pd.to_numeric(df['price'].replace('[\$,]', '', regex=True), errors='coerce')
    sorted_df = df.sort_values(by='price', ascending=False)
    return sorted_df

def most_expensive_neighborhood_group():
    pass

def most_expensive_neighborhood():
    pass

def most_popular_lists_by_reviews():
    pass

def most_popular_neighborhood_groups():
    pass


def most_popular_neighborhoods():
    pass


def host_with_most_listings():
    pass


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


frame = framing()
