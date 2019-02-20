Pyphilote
===========================================

Pyphilote (pronounced PIE-filla-tee) is a simple client library for the
Philote pubsub server (https://github.com/pote/philote).

Because Pyphilote relies on coroutines for concurrency, CPython 3.4 or above
is required to use it. CPython 3.6 or above is recommended.

The Philote server (source code and precompiled binaries for several
architectures) can be downloaded from https://github.com/pote/philote

The server can be started from the command line with an optional
shared secret for increased security.

For example::

    SECRET=SECRETKEY ./philote

To install the Python client package, run the following command in the
project's root directory::

    pip install .

or::

    python setup.py install

The following example uses the async/await syntax new in Python 3.5.
For more examples, see
https://github.com/taibende/pyphilote/tree/master/examples ::

    from pyphilote.network import Philote

    async def send():
        async with Philote(secret_key='SECRETKEY') as philote:
            await philote.send('test', 'Hello, world!')
