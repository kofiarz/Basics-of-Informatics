import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import pyqtgraph as pg
import numpy as np
import pandas as pd
from scipy import signal
from scipy.fft import fft
from scipy.io.wavfile import write

class App(QWidget):
     def __init__(self):
        super().__init__()

# Basic informations

        self.setWindowTitle("Signal Generator")
        self.setGeometry(100, 100, 1140, 850)
        self.setWindowIcon(QIcon('signal.jpg'))

# Structure

        siatka = QGridLayout()
        radiobuttons = QVBoxLayout()
        parameters = QGridLayout()
        buttons = QVBoxLayout()

# (0,0) - RadioButtons

        self.rb1 = QRadioButton("Sine")
        self.rb2 = QRadioButton("Square")
        self.rb3 = QRadioButton("Sawtooth")
        self.rb4 = QRadioButton("Triangle")
        self.rb5 = QRadioButton("White noise")

        self.rb1.setChecked(True)
        radiobuttons.addWidget(self.rb1)
        radiobuttons.addWidget(self.rb2)
        radiobuttons.addWidget(self.rb3)
        radiobuttons.addWidget(self.rb4)
        radiobuttons.addWidget(self.rb5)

# (0,1) - DoubleSpinBoxes

        self.length_label = QLabel("Length (t)")
        self.sampling_label = QLabel("Sampling (Hz)")
        self.amplitude_label = QLabel("Amplitude (m)")
        self.frequency_label = QLabel("Frequency (Hz)")
        self.length = QDoubleSpinBox()
        self.sampling = QDoubleSpinBox()
        self.sampling.setRange(0,50000)
        self.amplitude = QDoubleSpinBox()
        self.frequency = QDoubleSpinBox()
        self.frequency.setRange(0,50000)

        self.length.setValue(0.1)
        self.sampling.setValue(44100)
        self.amplitude.setValue(0.1)
        self.frequency.setValue(200)

        parameters.addWidget(self.length_label, 0, 0)
        parameters.addWidget(self.sampling_label, 1, 0)
        parameters.addWidget(self.amplitude_label, 2, 0)
        parameters.addWidget(self.frequency_label, 3, 0)
        parameters.addWidget(self.length, 0, 1)
        parameters.addWidget(self.sampling, 1, 1)
        parameters.addWidget(self.amplitude, 2, 1)
        parameters.addWidget(self.frequency, 3, 1)

# (0,2) - Signal plot

        self.wykres1 = pg.PlotWidget()
        self.wykres1.setLabel('left', text='<font size = 3> Amplitude (m) </font>')
        self.wykres1.setLabel('bottom', text='<font size = 3> Time (s) </font> ')
        self.wykres1.setTitle('<font size = 5> Signal </font>')

# (1,1) - Buttons

        self.b1 = QPushButton('Generate', self)
        self.b2 = QPushButton('Save signal to .wav', self)
        self.b3 = QPushButton('Save signal to .csv', self)
        self.b4 = QPushButton('Save Fourier Transform to .csv', self)

        self.b1.clicked.connect(self.which_function)
        self.b2.clicked.connect(self.sound)
        self.b3.clicked.connect(self.save_signal)
        self.b4.clicked.connect(self.save_fourier_transform)

        buttons.addWidget(self.b1)
        buttons.addWidget(self.b2)
        buttons.addWidget(self.b3)
        buttons.addWidget(self.b4)

# (1,0) - Table

        self.table = QTableWidget(self)
        self.table.resize(300, 200)
        self.table.setRowHeight(1000,1000)

# (1,2) - Fourier Transform plot

        self.wykres2 = pg.PlotWidget()
        self.wykres2.setLabel('left', text='<font size = 3> Amplitude (m) </font>')
        self.wykres2.setLabel('bottom', text='<font size = 3> Frequency (Hz) </font> ')
        self.wykres2.setTitle('<font size = 5> Fourier Transform </font>')

# Application of all elements

        siatka.addLayout(radiobuttons, 0, 0)
        siatka.addLayout(parameters, 0, 1)
        siatka.addWidget(self.wykres1, 0, 2)
        siatka.addWidget(self.table, 1, 0)
        siatka.addLayout(buttons, 1, 1)
        siatka.addWidget(self.wykres2, 1, 2)

        self.setLayout(siatka)
        self.show()

# Functions

     def which_function(self):

        self.wykres1.clear()
        self.wykres2.clear()
        l = self.length.value()
        s = self.sampling.value()
        a = self.amplitude.value()
        f = self.frequency.value()
        x = np.linspace(0, l, int(l * s))
        y=0
        if self.rb1.isChecked():
           y = a * np.sin(2 * np.pi * f * x)
        elif self.rb2.isChecked():
           y = a * signal.square(2 * np.pi * f * x)
        elif self.rb3.isChecked():
           y = 2 * a / np.pi * np.arctan(np.tan(np.pi * f * x))
        elif self.rb4.isChecked():
           y = 2 * a / np.pi * np.arcsin(np.sin(2 * np.pi * f * x))
        elif self.rb5.isChecked():
           y = np.random.rand(len(x))
        audio_data = np.int16(y * 2 ** 15)
        self.table.setRowCount(len(x))
        self.table.setColumnCount(2)
        for i in range(0, len(x)):
           self.table.setItem(i, 0, QTableWidgetItem(str(x[i])))
           self.table.setItem(i, 1, QTableWidgetItem(str(audio_data[i])))
        self.plot = self.wykres1.plot(x, audio_data)
        N = len(x)
        dt = x[1] - x[0]
        yf = 2.0 / N * np.abs(fft(audio_data)[0:N // 2])
        xf = np.fft.fftfreq(N, d=dt)[0:N // 2]
        self.plot = self.wykres2.plot(xf, yf)
        self.x_export = x
        self.audio_data_export = audio_data
        self.xf_export = xf
        self.yf_export = yf
        self.s_export = s

     def sound(self):
         write('sound.wav', int(self.s_export), self.audio_data_export)

     def save_signal(self):
         info = pd.DataFrame({'x': self.x_export, 'y': self.audio_data_export})
         info.to_csv("signal.csv", index=False)

     def save_fourier_transform(self):
         info = pd.DataFrame({'x': self.xf_export, 'y': self.yf_export})
         info.to_csv("fourier_transform.csv", index=False)

app = QApplication(sys.argv)
ex = App()
app.exec_()