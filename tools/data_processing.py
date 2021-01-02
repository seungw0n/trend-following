from enum import Enum
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class Option(Enum):
    daily = 'daily'
    monthly = 'monthly'
    weekly = 'weekly'

def read_csv(code, opt: Option):
    path = os.path.join(os.pardir, 'data', opt.value, code + '.csv')
    df = pd.read_csv(path)
    return df

def graph_time_based(dataframe, y):
    date = dataframe['date'].to_numpy()
    y_axis = dataframe[y].to_numpy()
    plt.plot(date, y_axis)
    plt.xlabel('date')
    plt.ylabel(y)
    plt.show()

# df = read_csv('A000020', Option.monthly)
# graph_time_based(df, 'open')

