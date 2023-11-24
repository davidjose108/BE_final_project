import requests

url = "http://127.0.0.1:5000/createcard"

tarot_card_data = {
    "number": 23,
    "name": "The Queen",
    "description": "Authentic, brave, powerful",
    "is_birth_card": False,
}

response = requests.post(url, json=tarot_card_data)

print(response.status_code)
print(response.json())

