from datetime import datetime

from flask import Flask, jsonify, request

from database import client, collection, db
from models import TarotCard

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return {"message": "Welcome to your Tarot Journal"}


@app.route("/pick", methods=["GET"])
def get_random_tarot_card():
    # Fetch a random tarot card from the MongoDB collection
    random_card = collection.aggregate([{"$sample": {"size": 1}}])

    # Check if any card is returned
    if random_card.alive:
        card = list(random_card)[0]  # Extract the card from the cursor

        # Remove the _id field from the card
        card.pop("_id", None)

        # Return the tarot card as a JSON response
        return jsonify({"tarot_card": card})
    else:
        return jsonify({"error": "No tarot cards found"}), 404


@app.route("/allcards", methods=["GET"])
def get_all_tarot_cards():
    # Fetch all tarot cards from the MongoDB collection
    all_cards = list(collection.find({}, {"_id": False}))

    return jsonify({"tarot_cards": all_cards})


@app.route("/create_tarot_card", methods=["POST"])
def create_tarot_card():
    try:
        tarot_card_data = TarotCard(**request.json)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    # Process tarot_card_data and save it to the database
    # For example, you can use tarot_card_data.name, tarot_card_data.description, tarot_card_data.number, and tarot_card_data.is_birth_card
    result = collection.insert_one(tarot_card_data.dict())

    return jsonify(
        {
            "message": "Tarot card created successfully",
            "inserted_id": str(result.inserted_id),
        }
    )


@app.route("/delete_tarot_card", methods=["DELETE"])
def delete_tarot_card():
    card_name = request.args.get("name")

    if not card_name:
        return jsonify({"error": "Name parameter is required for deletion"}), 400

    result = collection.delete_one({"name": card_name})

    if result.deleted_count == 1:
        return jsonify({"message": f"Tarot card {card_name} deleted successfully"})
    else:
        return jsonify({"error": f"Tarot card {card_name} not found"}), 404


@app.route("/set_birth_card/<name>", methods=["PUT"])
def set_birth_card(name):
    print(f"Trying to update is_birth_card for {name}")

    # Update the 'is_birth_card' field to True for the given tarot card name
    result = collection.update_one({"name": name}, {"$set": {"is_birth_card": True}})
    return jsonify({"message": f"Tarot card {name} updated as birth card"})
    # print(f"Modified count: {result.modified_count}")

    # if result.modified_count == 1:
    #     return jsonify({"message": f"Tarot card {name} updated as birth card"})
    # else:
    #     return jsonify({"error": f"Failed to update tarot card {name}"}), 500


@app.route("/get_birth_card", methods=["POST"])
def get_birth_card():
    try:
        # Get the birthdate from the request JSON
        birthdate = request.json.get("birthdate")

        # Validate the format of the birthdate (assuming YYYY-MM-DD)
        datetime.strptime(birthdate, "%Y-%m-%d")

        # Calculate the sum of individual digits in the birthdate
        digit_sum = sum(int(digit) for digit in birthdate if digit.isdigit())

        # Map the digit sum to a number between 0 and 22
        birth_card_number = digit_sum % 23

        # Retrieve the tarot card corresponding to the birth card number
        tarot_card = collection.find_one({"number": birth_card_number})

        if tarot_card:
            return jsonify({"tarot_card": tarot_card})
        else:
            return jsonify({"error": "Failed to retrieve tarot card"}), 500

    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
