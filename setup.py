from setuptools import setup

setup(
    name='mongo-helpers',
    version='0.1',
    description='Wrapper functions for PyMongo to simplify EDA for Mongo databases',
    url='https://github.com/mnguyenngo/mongo-helpers',
    author='Nguyen Ngo',
    author_email='mnguyenngo@gmail.com',
    license='BSD-3',
    packages=['mongo_helpers'],
    install_requires=['pandas', 'pymongo']
)
