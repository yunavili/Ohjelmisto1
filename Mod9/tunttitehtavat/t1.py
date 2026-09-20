class Lentokone:
    def __init__(self, nimi, maksimi_bensa, nykyinen_bensa):
        self.nimi = nimi
        self.maksimi_bensa = maksimi_bensa
        self.nykyinen_bensa = nykyinen_bensa
    
    def tankkaa(self, litroja):
        self.nykyinen_bensa += litroja

    def tulosta_tiedot(self):
        print(f"Konella {self.nimi} on {self.nykyinen_bensa} litraa bensaa.")

class Lentokentta:

    def __init__(self, nimi):
        self.nimi = nimi
        self.koneet = []

    def lisaa_lentokonet(self, kone):
        self.koneet.append(kone)

    def tulosta_koneet(self):
        print(f"Lentokentän {self.nimi} koneet:")
        for kone in self.koneet:
            kone.tulosta_tiedot()
    

lentokone1 = Lentokone("AS1", 200, 0)
lentokone2 = Lentokone("AD6", 200, 197)

lentokone1.tankkaa(33)

lentokentta1 = Lentokentta("Kivenlahti")
lentokentta1.lisaa_lentokonet(lentokone1)
lentokentta1.lisaa_lentokonet(lentokone2)
lentokentta1.tulosta_koneet()
