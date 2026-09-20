import random

print("Tämä ohjelma simuloi autokilpailua..")

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self):
        muutos = random.randint(-10, 16)
        if self.tamanhetkinen_nopeus + muutos < 0:
            self.tamanhetkinen_nopeus = 0
        elif self.tamanhetkinen_nopeus + muutos >= self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        else:
            self.tamanhetkinen_nopeus += muutos
    
    def kulje(self, tunnit):
        self.kuljettu_matka += tunnit * self.tamanhetkinen_nopeus

    def toString(self):
        return f"{self.rekisteritunnus}"


autos = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]



def race (cars, distance: int): #typehint!
    while True:
        for auto in cars:
            auto.kiihdyta()
            auto.kulje(1)
            if auto.kuljettu_matka >= distance:
                print(f"{auto.toString()} voitti kilpailun!! {auto.kuljettu_matka}")
                return

def printResults(cars):
    print(f"\n{'Rekisteritunnus':<16} | {'Huippunopeus':<16} | {'Nykynopeus':<16} | {'Kuljettu matka'}")
    print("-" * 72)

    for auto in cars:
        print(
            f"{auto.rekisteritunnus:<16} | "
            f"{auto.huippunopeus:<11} km/h | "
            f"{auto.tamanhetkinen_nopeus:<11} km/h | "
            f"{auto.kuljettu_matka} km" 
        )

race(autos, 10000)
printResults(autos)

