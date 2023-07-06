import requests

url = "http://localhost:8000/api/v1/source_definitions/get"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic Z2FyeTpnYXJ5",
    "Cookie": "csrftoken=1DA7Pef1PDQtqcxtpcBmffZ2hIAUx5BQTENRuwZwupB534b14oFYCGPf1yEIUUUq",
}

response = requests.request("POST", url, headers=headers)

print(response.text)
