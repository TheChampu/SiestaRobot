import asyncio
import sys
from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from SiestaRobot import MONGO_DB_URI
from SiestaRobot.confing import get_int_key, get_str_key


MONGO_PORT = get_int_key("27017")
MONGO_DB_URI = get_str_key("MONGO_DB_URI")
MONGO_DB = "SiestaRobot"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, MONGO_PORT)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI, MONGO_PORT)
db = motor[MONGO_DB]
db = client["VainBot"]