from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["train"]
collection = db["test"]

collection.insert_one({"msg": "Hello from VS Code"})