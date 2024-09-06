import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='eku',
         password='password',
         autocommit=True
         )

def maakoodi(nimi):
    sql = f"SELECT iso_country FROM country where name='{nimi}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0 :
        for rivi in tulos:
            print(f"Maan {nimi} iso_country koodi on {rivi[0]} ja maa sijaitsee {rivi[1]}:ssa")

maa = input("Anna maan nimi mistä olet kiinnostunut: ")
maakoodi(maa)