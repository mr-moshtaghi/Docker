import requests

x = requests.get("https://api.github.com")

if x.status_code == 200:
    print("everything is oke")
