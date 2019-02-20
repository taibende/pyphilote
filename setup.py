from setuptools import setup

setup(
    name='pyphilote',
    version='0.1.0',
    packages=['pyphilote'],
    url='https://github.com/taibende/pyphilote',
    license='MIT',
    author='Simon Liu',
    author_email='taibende@126.com',
    description='A Python client for the Philote pubsub server',
    install_requires=[
        "PyJWT >= 1.7.1",
        "websockets >= 7",
    ],
)
