import random

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

class Race:
    def __init__(self, name, length, racers):
        self.name = name
        self.length = length
        self.racers = racers

    def hour(self):
        for car in self.racers:
            change = random.randint(-10, 15)
            car.kiihdytys(change)
            car.kulje(1)

    def situation(self):
        print("Rekisteri\t huippunopeus\t \t nopeus \t kuljettu matka")
        for j in racers:
            print(f"{j.numero:10s} {j.huippunopeus:10d}kp/h {j.nopeus:10d}kp/h {j.matka:12d}km")

    def over(self):
        assumption = False
        for i in self.racers:
            if i.matka > 8000:
                assumption = True
                break
        return assumption

racers = []

for i in range(1,11):
    numero = "ABC-"+str(i)
    nopeus = random.randint(100,200)
    j = Auto(numero, nopeus)
    racers.append(j)

ralli = Race("Romuralli", 8000, racers)
kesto = 0
loppu = False

while loppu != True:
    ralli.hour()
    loppu = ralli.over()
    kesto += 1
    if kesto % 10 == 0:
        print(f"Kilpailu on kestänyt {kesto} tuntia, tilanne:")
        ralli.situation()

print(f"Kilpailu päättyi. Kilpailu kesti {kesto} tuntia")
print("Lopputulokset: ")
ralli.situation()