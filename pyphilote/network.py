import asyncio
import json
import jwt
import websockets


class Philote(object):

    """
    This class implements all the basic functionality of a Philote
    client.
    """

    def __init__(
        self,
        host='127.0.0.1',
        port=6380,
        secret_key='',
        write_channels = 'test',
        read_channels = 'test'
    ):
        self.host = host
        self.port = port
        self.secret_key = secret_key

        if type(write_channels) != list:
            self.write_channels = [str(write_channels)]
        else:
            self.write_channels = [str(c) for c in write_channels]

        if type(read_channels) != list:
            self.read_channels = [str(read_channels)]
        else:
            self.read_channels = [str(c) for c in read_channels]

        self.websocket = None


    def format(self, channel, data):
        """
        This method returns a JSON-formatted string that can be sent to
        the Philote server.
        """
        return json.dumps({
            'channel': channel,
            'data': data,
            'event': 'message'
        })


    def generate_token(self):
        """
        Generate a JSON Web Token based on the server's secret key.

        This is used to authenticate with the server.
        """
        claims = {'write': self.write_channels,
                  'read': self.read_channels}
        return jwt.encode(claims, self.secret_key, algorithm='HS256').decode()


    @asyncio.coroutine
    def connect(self):
        self.websocket = yield from websockets.connect(
            'ws://%s:%s/?auth=%s' % (self.host, self.port,
                                     self.generate_token())
        )
        return self.websocket


    @asyncio.coroutine
    def send(self, channel, data):
        if channel in self.write_channels:
            yield from self.websocket.send(self.format(channel, data))
        else:
            return False


    @asyncio.coroutine
    def recv(self):
        if len(self.read_channels) > 0:
            response = yield from self.websocket.recv()
            return response


    @asyncio.coroutine
    def __aenter__(self):
        """
        This asynchronous context manager's __enter__ method should only
        be used with Python 3.5 or above
        """
        yield from self.connect()
        return self


    @asyncio.coroutine
    def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        This asynchronous context manager's __exit__ method should only
        be used with Python 3.5 or above
        """
        if self.websocket:
            yield from self.websocket.close()
