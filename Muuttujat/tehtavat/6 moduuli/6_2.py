import random

def noppa(tahkot):
    while True:
        noppa = random.randint(1,tahkot)
        print(f"Heitettii noppa, tulos oli {noppa}")
        if noppa == tahkot:
            break

noppa(int(input("Anna tahkojen määrä:")))