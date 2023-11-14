# Getting all necessary packages and libraries

from typing import List, Optional

from pydantic import BaseModel
from pymongo import MongoClient

# Creating the class for the Tarot Cards


class TarotCard(BaseModel):
    name: str
    number: int
    element: str
    raidersmith: bool
    crowley: bool
    description: str
    keywords: Optional[List[str]]
    journal: str
    occurancy: int


# creating the methods for manipulating the database


class TarotJournal:
    # Creating the connection to mongoDB
    connection = MongoClient(
        "mongodb+srv://davidjose108:cN9guYoIbJgnxyFb@cluster0.at2q4em.mongodb.net/?retryWrites=true&w=majority"
    )

    # Creating the connection to the database
    db = connection.tarotjournal
    collection = db.cardtarot

    # Creating the first "document" (Tarot Card)
    def insertCard(self, card: TarotCard):
        return self.collection.insert_one(
            {
                "name": card.name,
                "number": card.number,
                "element": card.element,
                "raidersmith": card.raidersmith,
                "crowley": card.crowley,
                "description": card.description,
                "keywords": card.keywords,
                "journal": card.journal,
                "occurancy": card.occurancy,
            }
        )

    def getCard(self, name: str):
        return self.collection.find({"name": name})

    def deleteCard(self, name: str):
        return self.collection.delete_one({"name": name})

    def updateCard(self, name: str, cardupdated: TarotCard):
        return self.collection.replace_one(
            {"name": name},
            {
                "name": cardupdated.name,
                "number": cardupdated.number,
                "element": cardupdated.element,
                "raidersmith": cardupdated.raidersmith,
                "crowley": cardupdated.crowley,
                "description": cardupdated.description,
                "keywords": cardupdated.keywords,
                "journal": cardupdated.journal,
                "occurancy": cardupdated.occurancy,
            },
        )
