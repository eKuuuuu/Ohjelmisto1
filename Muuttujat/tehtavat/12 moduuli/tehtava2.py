import requests

api_key = "db8839a6201604219adb8ddf96c20683"

city_name = input("Give a city: ")
city_name = city_name.lower()

api = (f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")

print(api)

try:
    vastaus = requests.get(api)
    if vastaus.status_code == 200:
        x = vastaus.json()
        celsius = (x ['main']['temp']) - 272.15
        print(f"{city_name} weather is around {round(celsius, 0)} celsius degrees") ## Muunetaan kelvineistä celsiuiuiksi
        weather = (x['weather'][0]['main'])
        weather = weather.lower()
        print(f"Weather is: {weather}")
except requests.exceptions.RequestException as e:
    print("Ei voinut suortttaa")

print("Tapahtuma on ohi")