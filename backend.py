import uvicorn
from fastapi import FastAPI

from tarotdeck import TarotCard, TarotJournal

app = FastAPI()
db = TarotJournal()


@app.get("/")
def root():
    return {"message": "Welcome to your Tarot Journal"}


@app.get("/card/{card_name}")
def getCardByName(card_name: str):
    return db.getCard(card_name)


@app.post("/card")
def addCard(card: TarotCard):
    db.insertCard(card)
    return {"message": "successful"}


@app.put("/card/raidersmith/{card_name}")
def makeCardRaiderSmith(card_name: str):
    cardupdated = db.getCharacter(card_name)
    cardupdated.raidersmith = True
    db.updateCard(card_name, cardupdated)
    return {"message": "successful"}


@app.put("/card/crowley/{card_name}")
def makeCardCrowley(card_name: str):
    cardupdated = db.getCard(card_name)
    cardupdated.crowley = True
    db.updateCard(card_name, cardupdated)
    return {"message": "successful"}


@app.delete("/card/{card_name}")
def deleteCard(card_name: str):
    db.deleteCard(name=card_name)
    return {"message": "successful"}


class TarotJournal:
    @staticmethod
    def startBackend():
        uvicorn.run(
            "backend:app", host="localhost", port=4557, reload=True, log_level="info"
        )
