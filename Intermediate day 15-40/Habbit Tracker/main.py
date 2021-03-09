import requests
from datetime import datetime


TOKEN = "b6w56fsdvfsdftbh5wwq34frd"
USERNAME = "denis"
GRAPH_ID = "graph1"

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": TOKEN,
    "username": "denis",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Create user, run one time
# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create a graph
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# Add pixel to the graph
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8.0",
}

response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)
