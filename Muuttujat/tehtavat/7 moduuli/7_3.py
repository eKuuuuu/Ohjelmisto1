

kentat = {}
while True:
    kentta = int(input("Jos haluat lisätä lentokentän, kirjoita 1. \nJos haluat hakea lentokenttiä, kirjoita 2. \nJos haluat listata kaikki lentokentät, kirjota 3. \nJos haluat lopetta ohjeilman, kirjoita 4. \nAnna syöte: "))
    if kentta == 4:
        print("Ohjelma loppuu")
        break
    elif kentta == 1:
        icao = input("Anna lentokentän ICAO-koodi:")
        lentoaseman_nimi = input("Mikä on lentoaseman nimi:")
        kentat[icao] = lentoaseman_nimi
        print("Uusi lentoasema lisätty")
    elif kentta == 2:
        icao_koodi = input("Anna lentokentän ICAO-koodi: ")
        if icao_koodi in kentat:
            print("Lentokentän nimi on: " + str(kentat[icao_koodi]))
        else:
            print("Lentoasemaa ei ole lisättyä viellä, tai ei löyty.")
    else:
        for icao in kentat:
            print(icao,":",kentat[icao])

