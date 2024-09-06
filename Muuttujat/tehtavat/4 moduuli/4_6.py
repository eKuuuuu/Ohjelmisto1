import random

def pi(pisteiden_maara):
    ympyraan_osuneet = 0
    i = 0  #

    while i < pisteiden_maara:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x*x + y*y < 1:
            ympyraan_osuneet += 1

        i += 1

    pi_likiarvo = 4 * (ympyraan_osuneet / pisteiden_maara)
    return pi_likiarvo

pisteiden_maara = int(input("Anna pisteiden määrä: "))
piin_arvio = pi(pisteiden_maara)
print(f"Piin likiarvo {pisteiden_maara} pisteellä on noin: {piin_arvio}")
