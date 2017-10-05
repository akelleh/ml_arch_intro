from sklearn.linear_model import LinearRegression
from database import get_data
import pickle

class ModelHandler(object):
    # presumably, this should just live in a shared library
    def __init__(self, init_model=False):
        if init_model:
            self.model = self.load_model()

    def load_model(self):
        with open('model.pkl', 'rb') as fp:
            self.model = pickle.load(fp)
        return self.model

    def save_model(self, model):
        with open('model.pkl', 'wb') as fp:
            pickle.dump(model, fp)

def train_model(x_columns=['x'], y_column='y', N=1000):
    training_data = get_data(N)
    X = training_data[x_columns]
    y = training_data[y_column]
    model = LinearRegression().fit(X, y)
    print(model.coef_)
    return model
