import asyncio
from pyphilote.network import Philote


"""
This example uses the new async/await syntax from Python 3.5.
"""

secret_key = 'SECRETKEY'
pubsub_channel = 'ch1'


async def send():
    async with Philote(secret_key=secret_key,
                       read_channels=[pubsub_channel],
                       write_channels=[pubsub_channel]) as philote:
        for i in range(10):
            await philote.send(pubsub_channel, 'message %s' % i)


async def listener():
    async with Philote(secret_key=secret_key,
                       read_channels=[pubsub_channel],
                       write_channels=[pubsub_channel]) as philote:
        for i in range(10):
            msg = await philote.recv()
            print(msg)


if __name__ == '__main__':

    asyncio.ensure_future(send())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(listener())