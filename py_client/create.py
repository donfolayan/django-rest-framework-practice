import requests
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This is a title",
    "price": 22.39,
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())