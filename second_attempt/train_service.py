from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop, PeriodicCallback

from model import train_model, ModelHandler


def train_and_save():
    model = train_model()
    handler = ModelHandler()
    handler.save_model(model)

if __name__ == "__main__":
    PeriodicCallback(train_and_save, 1. * 1000.).start()
    IOLoop.current().start()
