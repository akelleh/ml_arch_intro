import nsq
from sklearn.linear_model import SGDRegressor

from model import ModelHandler

online_model = SGDRegressor(learning_rate='constant')
batch_size = 100
X_batch = []
y_batch = []
def message_handler(message):
    # assume message looks like {'x': [0.123], 'y': 1.2, 'type': 'train_event'}
    if message['type'] == 'train_event':
        global X_batch
        global y_batch
        X_batch.append(message['x'])
        y_batch.append(message['y'])
        if len(X_batch) == batch_size:
            online_model.partial_fit(X_batch, y_batch)
            X_batch = []
            y_batch = []
            model_handler.save(online_model)
    return True

if __name__ == "__main__":
    reader = nsq.Reader('training_events',
                        'my_models_events,
                        message_handler=message_handler)
    nsq.run()
