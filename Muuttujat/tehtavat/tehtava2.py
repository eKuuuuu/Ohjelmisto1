import random


def nimi():
    nimi = input("Anna nimesi: ")
    print("Terve, " +nimi + "!")

def ympyra():
    sade = float(input("Mikä on ympyrän säde?"))
    pintaala = 3.14 * (sade*sade)
    print("Ympyrän pinta-ala on ", pintaala)

def suorakulmuio():
    korkeus = int(input("Anna suorakulmion korkeus:"))
    kanta = int(input("Anna kannan korkeus:"))
    print(f"Piiri on {korkeus*2+kanta*2} suorakulmuio,ja pinta-ala on {kanta*korkeus}")

def kokonaisluvut():
    x = int(input("Anna ensimmäinen kokonaisluku: "))
    y = int(input("Anna toinen kokonaisluku: "))
    z = int(input("Anna kolmas kokonaisluku: "))
    summa = x + y + z
    tulo = x * y * z
    keskiarvo = summa / 3
    print(summa, tulo, keskiarvo)

def massa():
    leivi = float(input("Anna leiviskät:"))
    paino1 = leivi * 20 * 32 * 13.3
    naulat = float(input("Anna naulat:"))
    paino2 = naulat * 32 * 13.3
    luodit = float(input("Anna luodit:"))
    paino3 = luodit * 13.3

    yhtenainen = paino1 + paino2 + paino3
    print(yhtenainen)
    kilogrammat = yhtenainen/1000
    int_kilogrammat = int(kilogrammat)
    int_kilogrammat = int_kilogrammat * 1000
    grammat = yhtenainen - int_kilogrammat
    grammat = round(grammat, 2)

    print("Massa nykymittojen mukaan:")
    print(f"{int(kilogrammat)} kilogrammaa ja {grammat} grammaa")

def arpa():
    kolmenumeroinen = "".join([str(random.randint(0,9)) for _ in range(3)])
    neljanumeroinen = "".join([str(random.randint(1,6)) for _ in range(4)])
    print(kolmenumeroinen)
    print(neljanumeroinen)

nimi()
ympyra()
suorakulmuio()
kokonaisluvut()
massa()
arpa()
