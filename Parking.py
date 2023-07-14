#STWORZENIE KLAS

class Samochod():

    zaparkowany = "Nie"

    def __init__(self, numer_rejestracyjny, kolor, typ_pojazdu):
        self.numer_rejestracyjny = numer_rejestracyjny
        self.kolor = kolor
        self.typ_pojazdu = typ_pojazdu

    def wjazd_na_parking(self, parking):
        parking.wjazd(self)
        self.zaparkowany = "Tak"

    def wyjazd_z_parkingu(self, parking):
        parking.wyjazd(self)
        self.zaparkowany = "Nie"

    def info(self):
        print("Numer rejestracyjny: ", self.numer_rejestracyjny, "\nKolor: ", self.kolor, "\nTyp_pojazdu: ", self.typ_pojazdu, "\nCzy zaparkowany: ", self.zaparkowany)


class Parking():

    calkowita_liczba_miejsc = 5
    liczba_zajetych_miejsc = 0
    utarg = 0

    osobowy = []
    ciezarowy = []
    jednoslad = []

    def wjazd(self, samochod):
        if self.liczba_zajetych_miejsc < self.calkowita_liczba_miejsc:
            if samochod.typ_pojazdu == "osobowy":
                self.osobowy.append(samochod.numer_rejestracyjny)
            elif samochod.typ_pojazdu == "ciężarowy":
                self.ciezarowy.append(samochod.numer_rejestracyjny)
            elif samochod.typ_pojazdu == "jednoślad":
                self.jednoslad.append(samochod.numer_rejestracyjny)
            self.liczba_zajetych_miejsc += 1
        else:
            print("Nie można zaparkować - parking jest pełny.")

    def wyjazd(self, samochod):
        if samochod.typ_pojazdu == "osobowy":
            self.utarg += 10
        elif samochod.typ_pojazdu == "ciężarowy":
            self.utarg += 30
        elif samochod.typ_pojazdu == "jednoślad":
            self.utarg += 5
        self.liczba_zajetych_miejsc -= 1

    def info_liczba_zajetych_miejsc(self):
            print("Liczba zajętych miejsc: ", self.liczba_zajetych_miejsc)

    def info_utarg(self):
            print("Bieżący utarg: ", self.utarg)

    def info_lista(self, x):
        for i in range(len(x)):
            if i != len(x) - 1:
                print(x[i], end=", ")
            else:
                print(x[i])


# STWORZENIE OBIEKTÓW

samochod_1 = Samochod("KR83010", "zielony", "osobowy")
samochod_2 = Samochod("KRA99332", "czarny", "osobowy")
samochod_3 = Samochod("KWI47392", "różowy", "ciężarowy")
samochod_4 = Samochod("KMY85905", "niebieski", "ciężarowy")
samochod_5 = Samochod("KNT62909", "szary", "jednoślad")
samochod_6 = Samochod("KWA21370", "biały", "jednoślad")

parking = Parking()


# FUNKCJA TESTUJĄCA

samochod_1.wjazd_na_parking(parking)
samochod_2.wjazd_na_parking(parking)
samochod_3.wjazd_na_parking(parking)
samochod_2.wyjazd_z_parkingu(parking)

parking.info_liczba_zajetych_miejsc()

samochod_2.wjazd_na_parking(parking)
samochod_4.wjazd_na_parking(parking)
samochod_5.wjazd_na_parking(parking)

parking.info_liczba_zajetych_miejsc()
parking.info_utarg()

samochod_6.wjazd_na_parking(parking)
samochod_1.wyjazd_z_parkingu(parking)
samochod_6.wjazd_na_parking(parking)

parking.info_liczba_zajetych_miejsc()
parking.info_utarg()

samochod_2.wyjazd_z_parkingu(parking)
samochod_3.wyjazd_z_parkingu(parking)
samochod_4.wyjazd_z_parkingu(parking)
samochod_5.wyjazd_z_parkingu(parking)
samochod_6.wyjazd_z_parkingu(parking)

parking.info_liczba_zajetych_miejsc()
parking.info_utarg()

print("Wszystkie wjazdy samochodów na parking: ", end="")
parking.info_lista(parking.osobowy + parking.ciezarowy + parking.jednoslad)
print("Wjazdy samochodów ciężarowych na parking: ", end="")
parking.info_lista(parking.ciezarowy)




