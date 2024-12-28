import requests
response = requests.post(
    "https://dummyapi.io/data/v1/user/",
    headers={"app-id": "62b0433d2dfd91d4bf56c584"
    }
)
data = response.json()
print(data)
# result = data["data"][0]
# print(data)