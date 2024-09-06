import mysql.connector

def maakoodi(nimi):
    sql = f"SELECT iso_country, continent FROM country where name='{nimi}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for rivi in tulos:
        print(f"Maan {nimi} iso_country koodi on {rivi[0]} ja maa sijaitsee {rivi[1]}:ssa")## __ = {rivi[1]}

def tietokannat(sql):
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='eku',
         password='password',
         autocommit=True
         )

maa = input("Anna maan nimi mistä olet kiinnostunut: ")
maakoodi(maa)
sql = f"SELECT iso_country, continent FROM country where name='{maa}'"
tulos = tietokannat(sql)
for rivi in tulos:
    print(f"Maan {maa} iso_country koodi on {rivi[0]} ja maa sijaitsee {rivi[1]}:ssa")  ## __ = {rivi[1]}