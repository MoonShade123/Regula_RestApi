import requests


BASE = "http://127.0.0.1:5000/"

data = [{"title": "Created", "body": "Nice one", "likes": 1},
        {"title": "Ouch", "body": "Nice two", "likes": 10},
        {"title": "Not really", "body": "Nice three", "likes": 20}]

for i in range(len(data)):
    response = requests.put(BASE + "getrequest/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "getrequest/2")
print(response.json())
input()
response = requests.patch(BASE + "getrequest/2", {"body": "New one"})
print(response.json())
input()
response = requests.get(BASE + "getrequest/2")
print(response.json())

