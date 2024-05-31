import requests
from datetime import datetime

today = datetime.now()

# Constants and endpoints.
# --------------------------------
USERNAME = "name"
TOKEN = "token"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_input_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
graph_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# --------------------------------

# Header dictionary
headers = {
    "X-USER-TOKEN": TOKEN
}
# --------------------------------

# Making a new account
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text) # Commenting this out because the account has been made.
# --------------------------------

# Making a new graph and giving it a name and colour.
graph_config = {
    "X-USER-TOKEN": TOKEN,
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hr",
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers) # websites recommend headers cuz its
# safe
# print(response.text)
# --------------------------------

# Inputting values in graph
graph_input = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today?\n")
    }

response = requests.post(url=graph_input_endpoint, json=graph_input, headers=headers)
print(response.text)

# We can also use other HTTP requests such as put (to edit existing values) and delete (to delete existing values).



