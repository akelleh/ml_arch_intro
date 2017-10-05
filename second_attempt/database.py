
import numpy as np
import pandas as pd

def get_data(N=1000):
    x = np.random.normal(size=N)
    y = 2. * x + np.random.normal(size=N)
    return pd.DataFrame({'x': x, 'y': y})[['x', 'y']]
