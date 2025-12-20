import requests

TOKEN=""
headers = {

"Authorization": f"Bearer {TOKEN}",

"Accept": "application/"

}


url = "https://reqres.in/api/users/2"


response = requests.put(url, headers=headers)

print("Status Code:", response.status_code)

print("Response:")

print(response.json())
