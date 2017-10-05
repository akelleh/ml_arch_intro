from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop, PeriodicCallback

from model import ModelHandler

class PredictHandler(RequestHandler):
    def get(self):
        x = float(self.get_argument('x'))
        y = self.application.model_handler.model.predict(x)
        self.write('{}'.format(y))

class ModelApplication(Application):
    def __init__(self, handler_mapping):
        self.model_handler = ModelHandler(init_model=True)
        super(ModelApplication, self).__init__(handler_mapping)

if __name__ == "__main__":
    handler_mapping = [
                       (r'/predict$', PredictHandler),
                      ]
    application = ModelApplication(handler_mapping)
    application.listen(7777)
    PeriodicCallback(application.model_handler.load_model, 1. * 1000.).start()
    IOLoop.current().start()
