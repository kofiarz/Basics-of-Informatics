import numpy as np
def sense(x):
    while True:
        try:
            x=float(x)
            if x>0:
                return x
            else:
                x=float(input("Liczba musi być większa od 0. Spróbuj jeszcze raz: "))
        except:
            x=float(input("Należy wpisać liczbę. Spróbuj jeszcze raz: "))
def sense2(x):
    while True:
        try:
            x=int(x)
            if x in [0, 1, 2, 3, 4, 5, 6]:
                return x
            else:
                x = int(input("Liczba musi być jedną z podanych na liście. Spróbuj jeszcze raz: "))
        except:
            x = int(input("Należy wpisać liczbę całkowitą. Spróbuj jeszcze raz:  "))
def sc(x):
    return sense(input(x))
def menu():
    print("\nKALKULATOR PARAMETRÓW BRYŁ (Obowiązują jednostki układu SI)")
    print("1 - kula \n2 - czworościan foremny \n3 - ostrosłup prosty (o podstawie prostokątnej) \n4 - stożek \n5 - walec \n6 - elipsoida \n0  - ZAMKNIJ")
    choice = sense2((input("Wybierz polecenie, podając odpowiedni numer: ")))
    return choice
class Mass():
    def mass(self):
        return self.volume()*self.rho
    def describe(self):
        print("Obliczone parametry dla", self.name, "to:\nPole:", self.surface(), "m2", "\nObjętość:" ,self.volume(),"m3" ,"\nMasa:", self.mass(), "kg")
class Ball(Mass):
    def __init__(self, r, rho, name = "Bryła"):
        self.r = r
        self.rho = rho
        self.name = name
    def surface(self):
        return 4*np.pi*self.r**2
    def volume(self):
        return (4/3)*np.pi*self.r**3
class Regular_tetrahedron(Mass):
    def __init__(self, a, rho, name = "Bryła"):
        self.a = a
        self.rho = rho
        self.name = name
    def surface(self):
        return (self.a**2)*np.sqrt(3)
    def volume(self):
        return ((self.a**3)*np.sqrt(2))/12
class Simple_pyramid_with_rectangular_base(Mass):
    def __init__(self, a, b, h, rho, name = "Bryła"):
        self.a = a
        self.b = b
        self.h = h
        self.rho = rho
        self.name = name
    def surface(self):
        return self.a*self.b+(self.a*np.sqrt(((self.b/2)**2)*(self.h**2)))+(self.b*np.sqrt(((self.a/2)**2)*(self.h**2)))
    def volume(self):
        return (self.a*self.b*self.h)/3
class Cone(Mass):
    def __init__(self, r, h, rho, name = "Bryła"):
        self.r = r
        self.h = h
        self.rho = rho
        self.name = name
    def surface(self):
        return np.pi*(self.r**2)+np.pi*self.r*np.sqrt(self.r**2+self.h**2)
    def volume(self):
        return np.pi*(self.r**2)*self.h/3
class Cylinder(Mass):
    def __init__(self, r, h, rho, name = "Bryła"):
        self.r = r
        self.h = h
        self.rho = rho
        self.name = name
    def surface(self):
        return np.pi*(self.r**2)*2+2*np.pi*self.r*self.h
    def volume(self):
        return np.pi*(self.r**2)*self.h
class Ellipsoid(Mass):
    def __init__(self, a, b, e, rho, name = "Bryła"):
        self.a = a
        self.b = b
        self.e = e
        self.rho = rho
        self.name = name
    def surface(self):
        return 2*np.pi*self.b*(self.b+(self.a/self.e)*np.arcsin(self.e))
    def volume(self):
        return np.pi*self.a*(self.b**2)*(4/3)

while True:
    solid_figure = menu()
    if solid_figure == 0:
        break
    elif solid_figure == 1:
        ball__ = Ball(sc("Promień w m: "), sc("Gęstość w kg/m3: "), name = "kuli")
        ball__.describe()
    elif solid_figure == 2:
        regular_tetrahedron__ = Regular_tetrahedron(sc("Krawędź boczna w m: "), sc("Gęstość w kg/m3: "), name = "czworościanu foremnego")
        regular_tetrahedron__.describe()
    elif solid_figure == 3:
        simple_pyramid_with_rectangular_base__ = Simple_pyramid_with_rectangular_base(sc("Pierwsza krawędź podstawy w m: "), sc("Druga krawędź podstawy w m: "), sc("Wysokość w m: "), sc("Gęstość w kg/m3: "), name = "ostrosłupa prostego o podstawie prostokątnej")
        simple_pyramid_with_rectangular_base__.describe()
    elif solid_figure == 4:
        cone__ = Cone(sc("Promień w m: "), sc("Wysokość w m: "), sc("Gęstość w kg/m3: "), name = "stożka")
        cone__.describe()
    elif solid_figure == 5:
        cylinder__ = Cylinder(sc("Promień w m: "), sc("Wysokość w m: "), sc("Gęstość w kg/m3: "), name = "walca")
        cylinder__.describe()
    elif solid_figure == 6:
        a = sc("Pierwsza półoś w m: ")
        b = sc("Druga półoś w m: ")
        tab = [a,b]
        tab.sort()
        tab.reverse()
        ellipsoid__ = Ellipsoid(tab[0], tab[1], np.sqrt(1-((tab[1]**2)/(tab[0]**2))), sc("Gęstość: "),  name = "elipsoidy")
        ellipsoid__.describe()
