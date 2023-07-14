from scipy.io.wavfile import read
from scipy.optimize import curve_fit
from scipy.fft import fft
import numpy as np
import matplotlib.pyplot as plt


def plots(x,y, xl, yl, n, left=0, right = 3):
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(n)
    plt.xlim(left,right)
    plt.plot(x, y)
    plt.show()


def plots2(D, xl, yl, n, left=0, right = 3):
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(n)
    plt.xlim(left,right)
    plt.plot(D[0], D[1])
    plt.show()


def fourier(t,y):
    N = len(t)
    dt = t[1] - t[0]
    yf = 2.0 / N * np.abs(fft(y)[0:N // 2])
    xf = np.fft.fftfreq(N, d=dt)[0:N // 2]
    return [xf, yf]


def func(t, A, f, g, phi):
    return A * np.sin(2 * np.pi * f * t + phi) * (np.e ** ((-1) * g * t))


#0. Wczytanie pliku i przyjęcie danych

g4 = read("G4.wav") #wczytanie pliku .wav
sampling = g4[0] #częstotliwość próbkowania
sample_count = len(g4[1]) #liczba próbek
time = sample_count/sampling #długość trwania


#1. Klasyczny wykres

t = np.linspace(0,time,sample_count) #wektor czasu
y = g4[1] #wektor wartości
plots(t,y,"time", "amplitude", "G4") #wyświetlenie wykresu w całej dziedzinie
plots2([t,y] ,"time", "amplitude", "G4 - range (0.7, 0.75)", 0.7, 0.75) #wyświetlenie wykresu z ograniczeniem na osi poziomej


#2. Wykres z dopasowaniem

t1 = np.delete(t, slice(0,int(0.55*sampling))) #ograniczenie dziedziny - wyeliminowanie ciszy
y1 = np.delete(y, slice(0,int(0.55*sampling))) #usunięcie odpowiadającym im wartości
p0=[0,392,0, 0] #wektor inicjalizujący

fit_params, covariance_matrix = curve_fit(func, t1, y1,p0=p0)
print("parametry fitowania: \na=", fit_params[0], "\nf=", fit_params[1], "\ng=", fit_params[2], "\nphi=", fit_params[3]) #pokazanie parametrów fitowania
plt.plot(t1,y1) #stworzenie wykresu bez dopasowania
plt.plot(t1, func(t1, *fit_params), "r") #stworzenie wykresu z dopasowaniem
plt.xlabel("time") #oś OX
plt.ylabel("amplitude") #oś OY
plt.title("G4 after fitting") #tytuł
plt.show() #wyświetlenie wykresu po dopasowaniu


#3. Wykres FFT

f = fourier(t,y)
plots2(fourier(t, y), "frequency", "amplitude", "G4 - FFT", 0, 10000) #wyświetlenie FFT
