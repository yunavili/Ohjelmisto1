import random

print("Tämä ohjelma simuloi autokilpailua.")

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeus_muutos):
        uusi_nopeus = self.tamanhetkinen_nopeus + nopeus_muutos
        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += tunnit * self.tamanhetkinen_nopeus

    def toString(self):
        return f"{self.rekisteritunnus}"
            
class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

    def get_lisatiedot(self):
        return f"{self.akkukapasiteetti} kWh"

class Polttomoottoriauto(Auto):
    
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        self.bensatankki = bensatankki
        super().__init__(rekisteritunnus, huippunopeus)
    
    def get_lisatiedot(self):
        return f"{self.bensatankki} l"

class Kilpailu:
    def __init__(self, nimi, pituus: int, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    
    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta()
            auto.kulje(1)

    
    def tulosta_tilanne(self):
        print(f"\nKiplailu {self.nimi}")   
        print(f"\n{'Rekisteritunnus':<16} | {'Huippunopeus':<16} | {'Nykynopeus':<16} | {'Kuljettu matka'}")
        print("-" * 72)

        for auto in self.autot:
            print(
                f"{auto.rekisteritunnus:<16} | "
                f"{auto.huippunopeus :<11} km/h | "
                f"{auto.tamanhetkinen_nopeus:<11} km/h | "
            f"{auto.kuljettu_matka} km" 
            )

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False #early return


sahkoauto = Polttomoottoriauto("ABC-15", 180, 52.5)
polttoauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdyta(100)
polttoauto.kiihdyta(150)

sahkoauto.kulje(3)
polttoauto.kulje(3)

print(f"Sähköauto ({sahkoauto.rekisteritunnus}, {sahkoauto.get_lisatiedot()}): {sahkoauto.kuljettu_matka} km")
print(f"Polttomoottoriauto ({polttoauto.rekisteritunnus}, {polttoauto.get_lisatiedot()}): {polttoauto.kuljettu_matka} km")

