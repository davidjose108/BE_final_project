from pymongo import MongoClient

connection_string = (
    "mongodb+srv://davidjose108:cN9guYoIbJgnxyFb@cluster0.at2q4em.mongodb.net/"
)

client = MongoClient(connection_string)
db = client["tarot_deck"]
collection = db["major_arcana"]
