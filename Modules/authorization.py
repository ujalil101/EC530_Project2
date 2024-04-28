import os
from pymongo import MongoClient
from dotenv import load_dotenv
import bcrypt

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
# using bcrypt to securely hash passwords and protect them from being exposed in case of a data breach
def insert_user_data(username, password):
    db = connect_to_mongodb()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_data = {
        'username': username,
        'password': hashed_password,
        'documents': []  #  an empty list of documents for now.
    }
    db.users.insert_one(user_data)


# check if username and password in db for login purposes
def verify_credentials(username, password):
    db = connect_to_mongodb()
    user = db.users.find_one({'username': username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return user
    return None

