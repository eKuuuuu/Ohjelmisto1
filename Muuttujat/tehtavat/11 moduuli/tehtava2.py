class Auto:
    def __init__(self, numero, huippunopeus):
        self.numero = numero
        self.huippunopeus = huippunopeus
        self.matka = 0
        self.nopeus = 0

    def kiihdytys(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.matka += self.nopeus * aika

class Sahkoauto(Auto):
    def __init__(self, numero, huippunopeus, akkukapasiteetti):
        super().__init__(numero, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, numero, huippunopeus, tankin_koko):
        super().__init__(numero, huippunopeus)
        self.tankin_koko = tankin_koko

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdytys(100)
polttomoottoriauto.kiihdytys(120)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauton ({sahkoauto.numero}) matkamittari: {sahkoauto.matka} km")
print(f"Polttomoottoriauton ({polttomoottoriauto.numero}) matkamittari: {polttomoottoriauto.matka} km")
