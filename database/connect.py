from pymongo import MongoClient


client = MongoClient('mongodb://172.20.158.142:27017')
accidents_db = client['accidents_db']

monthly = accidents_db['monthly']
weekly = accidents_db['weekly']
daily = accidents_db["daily"]
area_colaction = accidents_db["area"]
