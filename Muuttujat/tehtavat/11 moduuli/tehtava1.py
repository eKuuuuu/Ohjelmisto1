class Kirjailija():
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Kirjailija):
    def __init__(self, nimi, kirjoittaja, sivut):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.maara = sivut

    def bookinfo(self):
        print("Kirjan tiedot")
        print(f"Nimi: {self.nimi}, kirjailija: {self.kirjoittaja}, sivujen lukumäärä: {self.maara}")

class Magazine(Kirjailija):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja

    def bookinfo(self):
        print("Lehden tiedot")
        print(f"Nimi: {self.nimi}, toimittaja: {self.toimittaja}")

magazine = Magazine("Aku Ankka", "Aki Hyppää")

kirja = Kirja("Hytti n:o 6", "Rosa Linksom", 200)

magazine.bookinfo()
kirja.bookinfo()