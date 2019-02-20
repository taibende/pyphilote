import asyncio
from pyphilote.network import Philote


"""
This example uses the old decorator syntax for coroutines from Python 3.4
"""


secret_key = 'SECRETKEY'
pubsub_channel = 'ch1'


@asyncio.coroutine
def send():

    philote = Philote(secret_key=secret_key,
                      read_channels=[pubsub_channel],
                      write_channels=[pubsub_channel])
    yield from philote.connect()
    for i in range(10):
        yield from philote.send(pubsub_channel, 'message %s' % i)
    yield from philote.websocket.close()


@asyncio.coroutine
def listener():

    philote = Philote(secret_key=secret_key,
                      read_channels=[pubsub_channel],
                      write_channels=[pubsub_channel])
    yield from philote.connect()
    for i in range(10):
        msg = yield from philote.recv()
        print(msg)
    yield from philote.websocket.close()


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    asyncio.ensure_future(send())
    asyncio.ensure_future(listener())
    # Run the program for 1 second.
    # This should give it enough time to shut down WebSocket connections
    # to the server
    loop.run_until_complete(asyncio.sleep(1))
