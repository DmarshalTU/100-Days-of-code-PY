# api https://opentdb.com/api.php

import requests

params = {
    "amount": 10,
    "type": "boolean",
}
response = requests.get("https://opentdb.com/api.php", params=params)
response.raise_for_status()
data = response.json()
question_data = data["results"]
