import math

def parempi_pizza(halkaisija, hinta):
    r = halkaisija/2
    pinta_ala = math.pi * r**2
    yksikkohinta = pinta_ala/hinta
    return yksikkohinta

pizza1 = parempi_pizza(int(input("Anna ensimmäisen pizzan halkaisija:")), int(input("Anna ensimmäisen pizzan hinta:")))

pizza2 = parempi_pizza(int(input("Anna toisen pizzan halkaisija:")), int(input("Anna toisen pizzaan hinta:")))

if pizza1 < pizza2:
    print("Toisen pizzan arvo on parempi.")
elif pizza1 == pizza2:
    print("Pizzat ovat samanarvoisia.")
else:
    print("Ensimmäisen pizzan arvo on parempi.")