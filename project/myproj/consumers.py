import json
from channels.generic.websocket import WebsocketConsumer
import time


class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are connected!'
        }))
