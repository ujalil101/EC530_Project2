import os
from pymongo import MongoClient
from dotenv import load_dotenv


# load password from .env file
load_dotenv()
pwd = os.getenv("password")

# connec to mongo
uri = f"mongodb+srv://ujalil:{pwd}@ec530proj2.hjuujqc.mongodb.net/?retryWrites=true&w=majority&appName=EC530Proj2"
def connect_to_mongodb():
    client = MongoClient(uri)
    db = client['EC530Proj2']
    return db 

# insert data
def insert_user_data(username, password):
    db = connect_to_mongodb()
    user_data = {
        'username': username,
        'password': password,
        #'email': email,
        'documents': []  #  an empty list of documents for now.
    }
    db.users.insert_one(user_data)

# check if username and password in db for login purposes
def verify_credentials(username, password):
    db = connect_to_mongodb()
    user = db.users.find_one({'username': username, 'password': password})
    return user is not None
