import random


def noppa():
    while True:
        noppa = random.randint(1,6)
        print(f"Heitettii noppa, tulos oli {noppa}")
        if noppa == 6:
            break

noppa()