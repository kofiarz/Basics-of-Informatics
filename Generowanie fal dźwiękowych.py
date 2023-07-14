import numpy as np
from scipy.io.wavfile import write
from scipy import signal
import matplotlib.pyplot as plt
from scipy.fft import fft
import pandas as pd

def TranformataFouriera(t,y):
    N = len(t)
    dt = t[1] - t[0]
    yf = 2.0 / N * np.abs(fft(y)[0:N // 2])
    xf = np.fft.fftfreq(N, d=dt)[0:N // 2]
    plt.plot(xf, yf)
    plt.xlabel("frequency (Hz)")
    plt.ylabel("amplitude")
    plt.show()
    data_new = {"t": xf, "y": yf}
    dataframe = pd.DataFrame(data_new)
    dataframe.to_csv("Przebieg.csv", index=False, sep="\t")
def sine(f,A):
    sampling = 44100
    time = 5
    t = np.linspace(0, time, time*sampling)
    data = A * np.sin(2 * np.pi * f * t)
    audio_data = np.int16(data * 2 ** 15)
    plt.plot(t, audio_data)
    plt.xlim(0, 0.01)
    plt.show()
    TranformataFouriera(t, data)
    write('sine.wav', sampling, audio_data)
def square(f,A):
    sampling = 44100
    time = 5
    t = np.linspace(0, time, time*sampling)
    data = A*signal.square(2*np.pi*f*t)
    audio_data = np.int16(data * 2 ** 15)
    plt.plot(t, audio_data)
    plt.xlim(0, 0.01)
    plt.show()
    TranformataFouriera(t, data)
def sawtooth(f,A,sampling, time):
    t = np.linspace(0, time, time*sampling)
    data = 2*A/np.pi * np.arctan(np.tan(np.pi * f * t))
    audio_data = np.int16(data * 2 ** 15)
    return t, audio_data
def triangle(f,A):
    sampling = 44100
    time = 5
    t = np.linspace(0, time, time*sampling)
    data = 2*A/np.pi * np.arcsin(np.sin(2 * np.pi * f * t))
    audio_data = np.int16(data * 2 ** 15)
    plt.plot(t, audio_data)
    plt.xlim(0, 0.01)
    plt.show()
def whitenoise(A):
    sampling = 44100
    time = 5
    t = np.linspace(0, time, time*sampling)
    data=np.random.rand(500)
    audio_data = np.int16(data * 2 ** 15)
    plt.plot(t[1:500], audio_data[1:500])
    plt.xlim(0, 0.01)
    plt.show()

sampling = 44100
# sine(440, 0.1)
# square(440,0.1)
t, audio_data = sawtooth(440,0.1, sampling, 5)
# triangle(440, 0.1)
# whitenoise(0.1)

TranformataFouriera(t, audio_data)
plt.plot(t, audio_data)
plt.xlim(0, 0.01)
plt.show()
write('test.wav', sampling, audio_data)

