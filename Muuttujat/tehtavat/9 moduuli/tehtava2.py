class Auto:
    def __init__(self, numero, huippunopeus):
        self.numero = numero
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
    def kiihdytys(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0
        return

car = Auto("ABC-123", 142)

print("Ajoneuvon tiedot:")
print(f"Ajoneuvon numero: {car.numero}")
print(f"Ajuneovon noepus: {car.nopeus}")
print(f"Noepus: {car.nopeus}, kuljettu matka: {car.matka}")

car.kiihdytys(30)
car.kiihdytys(50)
car.kiihdytys(70)

print(f"Ajoneuvon nopeus kiihdytykisen jälkeen: {car.nopeus}")

car.kiihdytys(-200)

print(f"Hätajarrutus! Ajoneuvon nopeus: {car.nopeus}")
