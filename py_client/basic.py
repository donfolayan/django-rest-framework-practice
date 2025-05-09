import requests

# endpoint = "https://www.httpbin.org/status/200"
# endpoint = "https://www.httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, params={"abc": 123}, json={"query": "Hello Test World"})
# print(get_response.text)
print(get_response.json())

# print(get_response.status_code)