import random
# Testing
class Auto:
    def __init__(self, numero, huippunopeus):
        self.numero = numero
        self.huippunopeus = huippunopeus
        self.matka = 0
        self.nopeus = 0

    def kiihdytys(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0
        return

    def kulje(self, aika):
        self.aika = aika
        self.matka += self.nopeus * aika
        return

kilpailjat = []

for i in range(1,11):
    numero = "ABC" + str(i)
    mspeed = random.randint(100,200)
    driver = Auto(numero, mspeed)
    kilpailjat.append(driver)

duration = 0
goal = 10000
continues = True

while continues:
    for driver in kilpailjat:
        change = random.randint(-10,15)
        driver.kiihdytys(change)
        driver.kulje(1)
        if driver.matka >= goal:
            continues = False
    duration += 1

print(f"Kilpailu päättyi, se kesti {duration} tuntia")

print("Rekkarit\t huippunopeus\t nopeus\t kuljettu matka\t")
for j in kilpailjat:
    print(f"{j.numero:10s} {j.huippunopeus:10d}kp/h {j.nopeus:10d}kp/h {j.matka:12d}km")


