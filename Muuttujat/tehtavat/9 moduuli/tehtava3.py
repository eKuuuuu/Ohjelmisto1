# Testing

class Auto:
    def __init__(self, numero, huippunopeus, matka):
        self.numero = numero
        self.huippunopeus = huippunopeus
        self.matka = matka
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

car = Auto("ABC-123", 142, 2000)

print("Ajoneuvon tiedot")
print(f"Ajoneuvon numero: {car.numero}")
print(f"Ajuneovon noepus: {car.nopeus}")
print(f"Noepus: {car.nopeus}, kuljettu matka: {car.matka}")

car.kiihdytys(60)
car.kulje(1.5)
print(f"Auto on kulkenut {car.matka} km, {car.aika} tunnin jälkeen")

