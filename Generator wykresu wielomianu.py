import numpy as np
import matplotlib.pyplot as plt

def wyswietl(parametr, potega):
    if parametr == 0:
        return ""
    elif parametr<0:
        return str(parametr) + "*x^" + str(potega)
    else:
        return "+"+str(parametr) + "*x^" + str(potega)

print("Witaj! Program służy do konstrukcji wykresu wielomianu czwartego stopnia postaci a*x^4 + b*x^3 + c*x^2 + d*x + e.")
a = int(input("Wprowadź wartość a: "))
b = int(input("Wprowadź wartość b: "))
c = int(input("Wprowadź wartość c: "))
d = int(input("Wprowadź wartość d: "))
e = int(input("Wprowadź wartość e: "))

wyniki = [wyswietl(a,4), wyswietl(b,3), wyswietl(c,2), wyswietl(d,1), wyswietl(e,0)]
wielomian = ' '.join(wyniki)
if "+" in wielomian[0:6]:
    wielomian = wielomian.replace("+", "",1)
wielomian = wielomian.replace("^1","")
wielomian = wielomian.replace("*x^0", "")
print("Twój wielomian to:", wielomian)

#ZAKRES WYŚWIETLANIA
# lx, rx = float(input("Podaj lewe ograniczenie wyswietlania osi OX: ")), float(input("Podaj prawe ograniczenie wyswietlania osi OX: "))
# if lx >= rx:
#     quit("Błąd!")
# by, uy = float(input("Podaj dolne ograniczenie wyswietlania osi OY: ")), float(input("Podaj górne ograniczenie wyswietlania osi OY: "))
# if by >= uy:
#     quit("Błąd!")
# zakres= [lx, rx, by, uy]
# plt.axis(zakres)

m=int(input("Podaj lewą granicę przedziału, dla którego ma zostać narysowany wykres: "))
n=int(input("Podaj prawą granicę przedziału, dla którego ma zostać narysowany wykres: "))

if m>=n:
    quit("Błąd!")

x = np.linspace(m, n, (n-m)*10000)
y = a*(x**4) + b*(x**3) + c*(x**2) + d*(x**1) + e

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykres wielomianu")
plt.xlim()
plt.show()





