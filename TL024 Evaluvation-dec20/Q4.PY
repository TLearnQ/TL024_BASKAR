import requests

def update_user_presence():
    api_url = "https://reqres.in/api/users/2"
    headers = {
        "Authorization": "Bearer reqres-token",
        "Content-Type": "application/json"
    }
    payload = {
        "job": "oracle"
    }

    response = requests.put(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        return "updatedAt exists" if "updatedAt" in data else "updatedAt missing"
    else:
        return f"Request failed with status {response.status_code}"


if __name__ == "__main__":
    print(update_user_presence())
