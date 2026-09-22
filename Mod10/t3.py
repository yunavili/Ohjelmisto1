class Hissi:
    def __init__(self, alin_kerros: int, ylin_kerros: int, numero: int):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.numero = numero
        self.kerros = 0

    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1

    def siirry_kerrokseen(self, kohdekerros: int):

        if kohdekerros > self.ylin_kerros or kohdekerros < self.alin_kerros:
            print(f"Rakennuksessa on kerroksia välillä {self.alin_kerros}-{self.ylin_kerros}")
            return

        if self.kerros == kohdekerros:
            print(f"Olet jo {self.kerros}. kerroksessa.")
            return

        while self.kerros > kohdekerros:
            self.kerros_alas()

        while self.kerros < kohdekerros:
            self.kerros_ylos()

        print(f"Hissi {self.numero} on {self.kerros}:lla kerroksella")


class Talo:
    def __init__(self, alin_kerros: int, ylin_kerros: int, hissien_luku: int):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.kerros = alin_kerros
        self.hissit = [ Hissi(alin_kerros, ylin_kerros, i+1) for i in range(hissien_luku)]

    def aja_hissia(self, hissin_num: int, kohdekerros: int):
        if hissin_num < 1 or hissin_num > len(self.hissit):
            print("Hissiä ei ole olemassa.")
            return

        print(f"\nAjetaan hissiä {hissin_num} kerrokseen {kohdekerros}")
        hissi = self.hissit[hissin_num - 1]
        hissi.siirry_kerrokseen(kohdekerros)

    def palohälytys(self):

        print("\nHissit on palohälytyksen vuoksi 1. kerroksessa")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(1)
            


talo = Talo(1, 14, 5)
talo.aja_hissia(1, 5)
talo.aja_hissia(5, 10)

talo.palohälytys()
talo.aja_hissia(7, 10)
