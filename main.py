from abc import ABC, abstractmethod

class Sutijums(ABC):
    def __init__(self, adresats, svars, izmers):
        if svars < 0:
            raise ValueError("Svars nevar būt negatīvs!")
        if izmers not in ("S", "M", "L"):
            raise ValueError("Izmēram jābūt 'S', 'M' vai 'L'")
        self.__adresats = adresats
        self.__svars = svars
        self.__izmers = izmers

    @property
    def adresats(self):
        return self.__adresats

    @property
    def svars(self):
        return self.__svars

    @property
    def izmers(self):
        return self.__izmers

    def pamattarifs(self):
        cenas = {"S": 2.00, "M": 4.00, "L": 6.00}
        return cenas[self.__izmers]

    @abstractmethod
    def aprekinat_cenu(self):
        pass

    def __str__(self):
        return f"Adresāts: {self.adresats}, svars: {self.svars} kg, izmērs: {self.izmers}, cena: {self.aprekinat_cenu()} €"

    def __lt__(self, other):
        return self.aprekinat_cenu() < other.aprekinat_cenu()


class ParastsSutijums(Sutijums):
    def aprekinat_cenu(self):
        return self.pamattarifs()


class TrauslsSutijums(Sutijums):
    def __init__(self, adresats, svars, izmers, iepakojuma_maksa):
        super().__init__(adresats, svars, izmers)
        self.__iepakojuma_maksa = iepakojuma_maksa

    def aprekinat_cenu(self):
        return self.pamattarifs() + self.__iepakojuma_maksa


class VertigsSutijums(Sutijums):
    def __init__(self, adresats, svars, izmers, vertiba):
        super().__init__(adresats, svars, izmers)
        self.__vertiba = vertiba

    def aprekinat_cenu(self):
        return self.pamattarifs() + self.__vertiba


class Pakomats:
    def __init__(self):
        self.sutijumi = []

    def pievienot_sutijumu(self, sutijums):
        self.sutijumi.append(sutijums)

    def aprekina_kopējo_cenu(self):
        return sum(s.aprekinat_cenu() for s in self.sutijumi)

    def paradit_visus(self):
        for s in self.sutijumi:
            print(s)

    def filtre_trauslos(self):
        return [s for s in self.sutijumi if isinstance(s, TrauslsSutijums)]

def main():
    pakomats = Pakomats()

    s1 = ParastsSutijums("Jānis Bērziņš", 2.5, 'M')
    s2 = TrauslsSutijums("Anna Kalniņa", 1.0, 'S', 2.0)
    s3 = VertigsSutijums("Pēteris Ozols", 0.8, 'L', 300)

    pakomats.pievienot_sutijumu(s1)
    pakomats.pievienot_sutijumu(s2)
    pakomats.pievienot_sutijumu(s3)

    #pakomats.paradit_visus()

    pakomats.paradit_visus()
    print("Kopējā cena:", pakomats.aprekina_kopējo_cenu(), "€")
    print("Vai s1 ir lētāks par s2?", s1 < s2)
    print("Trauslie sūtījumi:")
    for t in pakomats.filtre_trauslos():
        print(t, "Cena:", t.aprekinat_cenu(), "€")

if __name__ == "__main__":
    main()