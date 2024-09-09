from geopy import distance
import mysql.connector

def ICAO_koodi(icao):
    sql =  f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for rivi in tulos:
        latitude = rivi[0]
        longitude = rivi[1]
    return latitude, longitude
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='eku',
         password='password',
         autocommit=True
         )

syote1 = input("Anna etsivänä lentoaseman ICAO-koodi:")
cord1 = ICAO_koodi(syote1)
syote2 = input("Anna etsivänä lentoaseman ICAO-koodi:")
cord2 = ICAO_koodi(syote2)
etaisyys = distance.distance(cord1, cord2).km
print(f"Antamasi lentokenttien etäisyys on {etaisyys:.2f} kilometriä")