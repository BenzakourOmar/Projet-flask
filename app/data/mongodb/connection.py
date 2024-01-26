from pymongo import MongoClient
from config import Config

class Connection:
    def __init__(self):
        self.connection = MongoClient(Config.MONGO_URI)
