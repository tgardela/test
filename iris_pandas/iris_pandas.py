import pandas as pd
from pandas.core.frame import DataFrame
from typing import Dict


def is_input_float(input: str) -> bool:
    flag = False
    try:
        float(input)
        flag = True
    except ValueError as _:
        pass

    return flag

def read_data_from_url(url: str = None) -> DataFrame:
    '''Function for getting a DataFrame from a given URL'''
    if url is None:
        url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

    return pd.read_csv(url)


def describe(data: DataFrame = None) -> DataFrame:
    '''Function that returns the description of pandas DataFrame provided'''
    if data is None:
        data = read_data_from_url()

    return data.describe()


def sepal_length(length: float, data: DataFrame = None) -> Dict:
    '''Function that calculates the number of each species with the maximum sepal_length of given 'length' parameter'''
    if data is None:
        data = read_data_from_url()

    species_lengths = {species: 0 for species in data.species.unique()}

    for sp in species_lengths:
        species_lengths[sp] = str(data[(data.species == sp) & (data.sepal_length < length)].count().sepal_length)

    return species_lengths
