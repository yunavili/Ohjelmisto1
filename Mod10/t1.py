class Hissi:
    def __init__(self, alin_kerros: int, ylin_kerros: int):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.kerros = alin_kerros

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
 

        print(f"Hissi on {self.kerros}:lla kerroksella")


h = Hissi(0, 5)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(3)
h.siirry_kerrokseen(0)