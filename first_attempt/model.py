from sklearn.linear_model import LinearRegression
from database import get_data

class ModelHandler(object):
    def __init__(self, x_columns=['x'], y_column='y', N=1000):
        self.x_columns = x_columns
        self.y_column = y_column
        self.N = N
        self.model = self.get_model()

    def get_model(self):
        training_data = get_data(self.N)
        X = training_data[self.x_columns]
        y = training_data[self.y_column]
        self.model = LinearRegression().fit(X, y)
        print(self.model.coef_)
        return self.model
