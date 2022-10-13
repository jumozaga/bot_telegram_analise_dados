from matplotlib import docstring
import pandas as pd
import numpy as np


def transform_data(df):
    df['NPS interno'] = df['NPS interno'].str.replace(",", ".").astype("float")
    df.Setor = df.Setor.replace(
        {"Engenheiro de Software": "Engenharia de Software"})
    return df
