from main import collection

# Define a tarot card document
major_arcana_cards = [
    {
        "number": 1,
        "name": "The Magician",
        "description": "Manifestation, power, resourcefulness.",
        "is_birth_card": False,
    },
    {
        "number": 2,
        "name": "The High Priestess",
        "description": "Intuition, mystery, the subconscious.",
        "is_birth_card": False,
    },
    {
        "number": 3,
        "name": "The Empress",
        "description": "Nurturing, fertility, abundance.",
        "is_birth_card": False,
    },
    {
        "number": 4,
        "name": "The Emperor",
        "description": "Authority, structure, leadership.",
        "is_birth_card": False,
    },
    {
        "number": 5,
        "name": "The Hierophant",
        "description": "Tradition, spiritual guidance, education.",
        "is_birth_card": False,
    },
    {
        "number": 6,
        "name": "The Lovers",
        "description": "Love, relationships, choices.",
        "is_birth_card": False,
    },
    {
        "number": 7,
        "name": "The Chariot",
        "description": "Control, determination, victory.",
        "is_birth_card": False,
    },
    {
        "number": 8,
        "name": "Strength",
        "description": "Inner strength, courage, patience.",
        "is_birth_card": False,
    },
    {
        "number": 9,
        "name": "The Hermit",
        "description": "Solitude, introspection, wisdom.",
        "is_birth_card": False,
    },
    {
        "number": 10,
        "name": "Wheel of Fortune",
        "description": "Cycles, destiny, change.",
        "is_birth_card": False,
    },
    {
        "number": 11,
        "name": "Justice",
        "description": "Fairness, balance, legal matters.",
        "is_birth_card": False,
    },
    {
        "number": 12,
        "name": "The Hanged Man",
        "description": "Surrender, letting go, sacrifice.",
        "is_birth_card": False,
    },
    {
        "number": 13,
        "name": "Death",
        "description": "Transformation, change, renewal.",
        "is_birth_card": False,
    },
    {
        "number": 14,
        "name": "Temperance",
        "description": "Balance, moderation, harmony.",
        "is_birth_card": False,
    },
    {
        "number": 15,
        "name": "The Devil",
        "description": "Materialism, bondage, temptation.",
        "is_birth_card": False,
    },
    {
        "number": 16,
        "name": "The Tower",
        "description": "Destruction, upheaval, revelation.",
        "is_birth_card": False,
    },
    {
        "number": 17,
        "name": "The Star",
        "description": "Hope, inspiration, spirituality.",
        "is_birth_card": False,
    },
    {
        "number": 18,
        "name": "The Moon",
        "description": "Illusion, intuition, subconscious.",
        "is_birth_card": False,
    },
    {
        "number": 19,
        "name": "The Sun",
        "description": "Joy, success, vitality.",
        "is_birth_card": False,
    },
    {
        "number": 20,
        "name": "Judgment",
        "description": "Reckoning, transformation, rebirth.",
        "is_birth_card": False,
    },
    {
        "number": 21,
        "name": "The World",
        "description": "Completion, accomplishment, fulfillment.",
        "is_birth_card": False,
    },
    {
        "number": 0,
        "name": "The Fool",
        "description": "New beginnings, spontaneity, unpredictability.",
        "is_birth_card": False,
    },
]


# Insert the list of major arcana tarot cards into the collection
result = collection.insert_many(major_arcana_cards)

# Print the inserted documents' IDs
print(f"Inserted document IDs: {result.inserted_ids}")
