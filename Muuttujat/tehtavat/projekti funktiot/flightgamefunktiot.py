import mysql.connector
from geopy import distance
from random import randint



# =====================================================
# For example
def country_query(country):
    airport_country_list = []
    sql = f"SELECT airport.name FROM country INNER JOIN airport ON country.iso_country = airport.iso_country WHERE country.name = '{country}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        for row in result:
            airport_country_list.append(row[0])

        return airport_country_list

def city_query(country, city):
    airport_city_list = []
    sql = f"SELECT airport.name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country WHERE country.name = '{country}' AND airport.municipality = '{city}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        for row in result:
            airport_city_list.append(row[0])
        return airport_city_list

def airport_information(country, city, icao):
    sql = f"SELECT airport.name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country WHERE country.name = '{country}' AND airport.municipality = '{city}' AND airport.gps_code = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        for row in result:
            return row[0]
# =====================================================

# =====================================================
# Main tasks
def get_airports_by_country(country):
    airport_list = []
    sql = f"SELECT airport.name FROM airport INNER JOIN country ON airport.iso_country = country.iso_country WHERE country.name = '{country}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        for row in result:
            airport_list.append(row[0])

        return airport_list

# A database connection
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306, # Change your port to 3306 if necessary
    database="flight_game", # Enter your database name
    user="eku", # Enter your username
    password="password", # Enter your password
    autocommit=True
)

# =====================================================
# For example
program = input("(Y/N): ").upper()

if program == "Y":
    while True:
        country_input = input("Enter a country name: ").capitalize()
        country_list = country_query(country_input)
        if country_list:
            print(f"All airports in {country_input}:\n")
            for country in country_list:
                print(f"\t{country}")
            print("\n")
            break
        else:
            print("\nInvalid country, try again.\n")

    while True:
        city_input = input(f"Enter {country_input}'s city name: ").capitalize()
        city_list = city_query(country_input, city_input)
        if city_list:
            print(f"Airports found in the city: {city_input}\n")
            for city in city_list:
                print(f"\t{city}")
            print("\n")
            break
        else:
            print(f"\nInvalid city, please enter a city in {country_input} that has an airport.\n")

    while True:
        icao_input = input("Enter an icao code: ").upper()
        airport_name = airport_information(country_input, city_input, icao_input)
        if airport_name:
            print(f"Airport: {airport_name}\n")
            break
        else:
            print("\nInvalid icao code, please try again.\n")
else:
    print("Continuing...")
# =====================================================

# =====================================================
# Main tasks
while True:
    print("1 = Search country, 2 = Search city, 3 = Search an airport by ICAO, 4 = Random Destination Generator 5 = Stop the program: ")
    options = input("Enter your choice (1, 2, 3 or 4): ")

    if options == "1":
        search_country = input("Enter a country name: ").capitalize()
        airports = get_airports_by_country(search_country)
        print(airports)
    elif options == "2":
        print()



