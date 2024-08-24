import pandas as pd


def apply_transformations(df, transformations):
    if 'normalize' in transformations:
        for column in transformations['normalize']:
            df[column] = (df[column] - df[column].mean()) / df[column].std()
    if 'fill_missing' in transformations:
        for column, value in transformations['fill_missing'].items():
            df[column].fillna(value, inplace=True)
    return df
