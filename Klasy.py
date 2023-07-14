class Bike(): # Definicja klasy Bike
    vehicle_type = "two-wheeler" # Pole statyczne klasy
    def __init__(self, wheel, color): # konstruktor klasy Bike z argumentami
        self.wheel = wheel # pola klasy Bike
        self.color = color
    def wheel_get(self): # metoda klasy Bike, która zwraca wartość pola wheel, tzw. "getter"
        return self.wheel
    def color_get(self): # metoda klasy Bike, która zwraca wartość pola color, tzw. "getter"
        return self.color
    def color_set(self, new_color): # metoda klasy Bike, która ustawia wartość pola color, tzw. "setter"
        self.color = new_color

my_bike = Bike(2, "red") # obiekt klasy Bike

print(my_bike.vehicle_type) # wyświetlamy zmienna publiczną instancji (taka sama wartość niezalenie od obiektu)
print(my_bike.wheel_get()) # wyświetlamy atrybut wheel klasy Bike
print(my_bike.color_get()) # wyświetlamy atrybut color klasy Bike
my_bike.color_set("green") # zmieniamy atrybut klasy Bike
print(my_bike.color_get()) # ponownie wyświetlamy atrybut color klasy Bike

######################################################
class Car():
    wheels = 4
    engine = "Volvo"
    max_velocity = 220
    color = "black"
    seats = 5
    def get(self):
        return self.wheels, self.engine, self.max_velocity, self.color, self.seats
    def set(self, new_color):
        self.color = new_color

class Electric(Car):
    woltaz = "50V"
    dlugosc_kabla = "2137 m"
    def get_wszystko(self):
        print(Car.get(self))
        return self.wheels, self.engine, self.max_velocity, self.color, self.seats, self.woltaz, self.dlugosc_kabla

# Passat = Car()
# Golf = Car()
# Multipla = Car()
# print(Passat.get())
# Passat.set("green")
# print(Passat.get())
tesla = Electric()
print(tesla.get_wszystko())
#########################################################
class Ciasto():
    def __init__(self, wielkosc, smak):
        self.wielkosc = wielkosc
        self.smak = smak
    def informacja(self):
        print("To ciasto ma rozmiar " + self.wielkosc + " i smak " + self.smak)

class Tort(Ciasto):
    # def __init__(self, wielkosc, smak):
    #     Ciasto.__init__(self, wielkosc, smak)
    def Tort(self):
        print("Ten tort ma rozmiar " + self.wielkosc + " i smak " + self.smak)

ciasto_czekoladowe = Ciasto("średni", "czekoladowy") # obiekt klasy Ciasto
ciasto_czekoladowe.informacja() # wywołanie metody klasy Ciasto --> "To ciasto ma rozmiar średni i smak czekoladowy"

tort_truskawkowy = Tort("duży", "truskawkowy") # Obiekt klasy Tort dziedziczący metody i pola klasy Ciasto
tort_truskawkowy.Tort() # ---> "Ten tort ma rozmiar duży i smak truskawkowy"
tort_truskawkowy.informacja() # # ---> "To ciasto ma rozmiar duży i smak truskawkowy"
######################################################################
print("\n \n")
