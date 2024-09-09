import mysql.connector

def maakoodi(syote):
    sql =  f"SELECT type FROM airport WHERE iso_country='{syote}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    lista = []
    for i in tulos:
        lista.append(str(i))
    print(lista)
    pieni = lista.count("('small_airport',)")
    normi = lista.count("('medium_airport',)")
    iso = lista.count("('large_airport',)")
    heli = lista.count("('heliport',)")
    print(f"Antamasi valtioissa on {pieni} pieniä lentokenttiä, {normi} normi kokoisia lentokenttiä, {iso} isoja lentokenttijä ja heliportteja {heli}")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='eku',
         password='password',
         autocommit=True
         )

syote = input("Anna maakoodi: ")
maakoodi(syote)