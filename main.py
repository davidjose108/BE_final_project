from flask import Flask, jsonify, request

from database import client, collection, db
from models import TarotCard

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return {"message": "Welcome to your Tarot Journal"}


# CREATE a card
@app.route("/createcard", methods=["POST"])
def createcard():
    try:
        tarot_card_data = TarotCard(**request.json)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    result = collection.insert_one(tarot_card_data.model_dump())

    return jsonify(
        {
            "message": "Tarot card created successfully",
            "inserted_id": str(result.inserted_id),
        }
    )


# GET a card from the number
@app.route("/card/<int:card_number>", methods=["GET"])
def get_card_by_number(card_number):
    tarot_card = collection.find_one({"number": card_number})
    tarot_card.pop("_id", None)
    return jsonify({"tarot_card": tarot_card})


# GET a random card
@app.route("/pick", methods=["GET"])
def get_random_tarot_card():
    random_card = collection.aggregate([{"$sample": {"size": 1}}])
    if random_card.alive:
        card = list(random_card)[0]
        card.pop("_id", None)
        return jsonify({"tarot_card": card})
    else:
        return jsonify({"error": "No tarot cards found"}), 404


# GET the list of all cards (documents)
@app.route("/allcards", methods=["GET"])
def get_all_tarot_cards():
    all_cards = list(collection.find({}, {"_id": False}))
    return jsonify({"tarot_cards": all_cards})


# DELETE a card
@app.route("/delete_tarot_card", methods=["DELETE"])
def delete_tarot_card():
    card_name = request.args.get("name")
    result = collection.delete_one({"name": card_name})
    return jsonify({"message": f"Tarot card {card_name} deleted successfully"})


@app.route("/my_birth_card/<name>", methods=["PUT"])
def set_birth_card(name):
    # We want to first check the value of the card to know if it is true or false
    tarot_card = collection.find_one({"name": name})

    if tarot_card:
        current_value = tarot_card.get("is_birth_card", False)

        # Update the field to the opposite
        result = collection.update_one(
            {"name": name}, {"$set": {"is_birth_card": not current_value}}
        )
        return jsonify({"message": f"Tarot card {name} updated"})
    else:
        return jsonify({"error": f"Failed to update tarot card {name}"}), 500


@app.route("/my_birth_card", methods=["POST"])
def get_birth_card():
    try:
        # Get the birthdate from the request JSON
        birthdate = request.json.get("birthdate")
        # Calculate the sum of individual digits in the birthdate
        digit_sum = sum(int(digit) for digit in birthdate if digit.isdigit())
        print(digit_sum)
        # Map the digit sum to a number between 0 and 22
        birth_card_number = digit_sum % 23
        print(birth_card_number)
        # Retrieve the tarot card corresponding to the birth card number
        tarot_card = collection.find_one({"number": birth_card_number})

        if tarot_card:
            tarot_card["_id"] = str(tarot_card["_id"])
            return jsonify({"tarot_card": tarot_card})
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400


if __name__ == "__main__":
    app.run(debug=True)
