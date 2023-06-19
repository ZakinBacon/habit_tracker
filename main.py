import requests
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.getenv("TOKEN")
USERNAME = "zakin"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# ------------------------Create Graph --------------------------------------#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@zakin , it is your profile page!","isSuccess":true}


# ------------------------POST --------------------------------------#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "graph1"
graph_configuration = {
    "id": GRAPH_ID,
    "name": "Dog Walks",
    "unit": "min",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()
TODAY = today.strftime("%Y%m%d")
# response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
# print(response.text)
pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

pixel_configuration = {
    "date": TODAY,
    "quantity": "2",
}

# response = requests.post(url=pixel_endpoint, json=pixel_configuration,headers=headers)
# print(response.text)

# ------------------------Update --------------------------------------#
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

update_pixel_request = {
    "quantity": input("How long did you walk the dogs for today?"),
}

response = requests.put(url=update_pixel_endpoint, json=update_pixel_request, headers=headers)
response.raise_for_status()
print(response.text)

# ------------------------ delete --------------------------------------#

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"


# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# response.raise_for_status()
# print(response.text)