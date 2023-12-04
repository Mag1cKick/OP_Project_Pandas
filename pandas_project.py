"""pandas project"""
import pandas as pd

def framing():
    file = '/Users/bohdanpopov/Documents/GitHub/OP_Project_Pandas/train.csv'
    df = pd.read_csv(file)
    return df

frame = framing()
