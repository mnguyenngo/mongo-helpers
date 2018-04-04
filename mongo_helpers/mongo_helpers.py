from pymongo import MongoClient
import pandas as pd

def convert_db_to_df(db_name, collection_name, host='localhost', address=27017):
    """ Returns a dataframe given a database name and collection name.

        Args:
            db_name (str): name of database
            collection_name (str): name of collection
            host (str): 'localhost' (default) for mongodb on local computer
            address (int): '27017' (default) for mongodb on local computer

        Returns:
            df (pandas dataframe)
    """

    client = MongoClient(host, address)
    db = client[db_name]
    c = db[collection_name]
    df = pd.DataFrame(list(c.find()))
    return df

def get_db_names(host='localhost', address=27017):
    """ Returns a list of names of the databases available at the provided address.

        Args:
            host (str): 'localhost' (default) for mongodb on local computer
            address (int): '27017' (default) for mongodb on local computer

        Returns:
            list of database names
    """

    client = MongoClient(host, address)
    return client.database_names()

def get_collection_names(db_name, host='localhost', address=27017):
    """ Returns a list of the names of the collections at the specified database.

        Args:
            db_name (str): name of database
            host (str): 'localhost' (default) for mongodb on local computer
            address (int): '27017' (default) for mongodb on local computer

        Returns:
            list of collections names
    """
    client = MongoClient(host, address)
    db = client[db_name]
    return db.collection_names()
