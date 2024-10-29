import requests

api = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(api)

try:
    if vastaus.status_code == 200:
        x = vastaus.json()
        print(x ["value"])
except requests.exceptions.RequestException as e:
    print("Ei voinut suortttaa")

print("Tapahtuma on ohi")