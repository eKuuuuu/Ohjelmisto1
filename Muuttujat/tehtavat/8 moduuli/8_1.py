import mysql.connector

def ICAO_koodi(syote):
    sql =  f"SELECT name, iso_region FROM airport WHERE ident='{syote}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for rivi in tulos:
        print(f"ICAO koodi {syote} vastaa lentoasemaa {rivi[0]}, jonka sijantikunta on: {rivi[1]}")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='eku',
         password='password',
         autocommit=True
         )

syote = input("Anna etsivänä lentoaseman ICAO-koodi:")
ICAO_koodi(syote)