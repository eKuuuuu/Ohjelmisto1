class auto:
    def __init__(self, numero, nopeus):
        self.numero = numero
        self.nopeus = nopeus
        self.nopeus = 0
        self.matka = 0

car = auto("ABC-123", 142)

print("Ajoneuvon tiedot:")
print(f"Ajoneuvon numero: {car.numero}")
print(f"Ajuneovon noepus: {car.nopeus}")
print(f"{car.nopeus} + {car.matka}")
