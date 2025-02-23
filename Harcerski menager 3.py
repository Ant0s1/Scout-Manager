class Harcerz:
    def __init__(self, imie, nazwisko, stopien):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stopien = stopien
        self.zadania = []
        self.oceny = []

    def dodaj_zadanie(self, zadanie):
        self.zadania.append(zadanie)

    def wykonane_zadania(self):
        return [z for z in self.zadania if z["wykonane"]]
    
    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.stopien}"


class Druzyna:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.czlonkowie = []

    def dodaj_harcerza(self, harcerz):
        self.czlonkowie.append(harcerz)

    def lista_harcerzy(self):
        return [str(h) for h in self.czlonkowie]


class Zbiorka:
    def __init__(self, data, temat, prowadzacy):
        self.data = data
        self.temat = temat
        self.prowadzacy = prowadzacy
        self.obecni = []
        self.oceny = {}

    def dodaj_obecnego(self, harcerz):
        self.obecni.append(harcerz)
    
    def ocen_harcerza(self, harcerz, ocena):
        if harcerz in self.obecni:
            self.oceny[harcerz] = ocena
            harcerz.dodaj_ocene(ocena)

    def lista_obecnych(self):
        return [str(h) for h in self.obecni]


class Kalendarz:
    def __init__(self):
        self.zbiorki = []

    def dodaj_zbiorke(self, zbiorka):
        self.zbiorki.append(zbiorka)

    def wyswietl_kalendarz(self):
        return [f"{z.data}: {z.temat} (Prowadzący: {z.prowadzacy})" for z in self.zbiorki]


# Przykładowe użycie
harcerz1 = Harcerz("Jan", "Kowalski", "Wywiadowca")
harcerz2 = Harcerz("Anna", "Nowak", "Tropicielka")
harcerz3 = Harcerz("Antoni", "Zawadzki", "Odkrywca")

druzyna = Druzyna("Orły")
druzyna.dodaj_harcerza(harcerz1)
druzyna.dodaj_harcerza(harcerz2)
druzyna.dodaj_harcerza(harcerz3)

zbiorka = Zbiorka("2025-10-02", "Zbiórka Awaryjna", "Druhna Kasia, Druhna Emi, Druhna Ola, Druh Alan,")
zbiorka.dodaj_obecnego(harcerz1)
zbiorka.dodaj_obecnego(harcerz2)
zbiorka.dodaj_obecnego(harcerz3)
zbiorka.ocen_harcerza(harcerz1, 5)
zbiorka.ocen_harcerza(harcerz2, 4)
zbiorka.ocen_harcerza(harcerz3, 6)

kalendarz = Kalendarz()
kalendarz.dodaj_zbiorke(zbiorka)

print("Lista harcerzy w drużynie:", druzyna.lista_harcerzy())
print("Obecni na zbiórce:", zbiorka.lista_obecnych())
print("Oceny harcerzy:", {str(h): h.oceny for h in zbiorka.obecni})
print("Kalendarz zbiórek:", kalendarz.wyswietl_kalendarz())
