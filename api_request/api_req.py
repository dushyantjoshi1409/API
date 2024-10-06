import requests
response = requests.get("https:......")

detalis = response.json()
for i in range(len(detalis)):
    print(detalis[i])