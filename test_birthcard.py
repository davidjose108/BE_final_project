import unittest

from flask import json

from main import app


class TestBirthCardRoute(unittest.TestCase):
    def setUp(self):
        # Create a test client so I do not need to run the main file
        self.app = app.test_client()

    def test_get_birth_card_valid_dates(self):
        # Test case 1
        response1 = self.app.post("/my_birth_card", json={"birthdate": "19960123"})
        data1 = json.loads(response1.data.decode("utf-8"))
        # Without this line the data is raw bytes data
        self.assertEqual(data1["tarot_card"]["number"], 8)

        # Test case 2
        response2 = self.app.post("/my_birth_card", json={"birthdate": "19952209"})
        data2 = json.loads(response2.data.decode("utf-8"))
        self.assertEqual(data2["tarot_card"]["number"], 14)

        # Test case 3
        response3 = self.app.post("/my_birth_card", json={"birthdate": "20221116"})
        data3 = json.loads(response3.data.decode("utf-8"))
        self.assertEqual(data3["tarot_card"]["number"], 15)


if __name__ == "__main__":
    unittest.main()
