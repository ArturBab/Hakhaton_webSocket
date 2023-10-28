import json
from channels.generic.websocket import WebsocketConsumer
import time


depth = 0
oxygen = 100
fuel = 100


def submarine(move):
    global depth
    global oxygen  # в %
    global fuel  # в %
    while oxygen & fuel:
        if move:
            depth = depth - move
        if depth != 0:
            oxygen = oxygen - 5
        else:
            oxygen = 100
        fuel = fuel - 1
        yield ({'depth': depth, 'oxygen': oxygen, 'fuel': fuel})
        time.sleep(2)


class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print('Message:', message)