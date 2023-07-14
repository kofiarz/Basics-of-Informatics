from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt

data = read("piraci.wav") #import pliku .wav
sampling = data[0] #częstotliwość próbkowania
sample_count = len(data[1]) #liczba próbek
time = sample_count/sampling #długość trwania
t = np.linspace(0,time,sample_count) #wektor czasu
plt.specgram(data[1], 20000, data[0]) #spektogram
plt.ylim(250,650) #ograniczenie wyświetlania na osi pionowej
plt.xlabel("time") #oś OX
plt.ylabel("frequency") #oś OY
plt.title("Pirates of the Caribbean - spectogram") #tytuł
plt.show() #wyświetlenie spektogramu