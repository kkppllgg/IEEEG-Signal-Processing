import numpy as np
from scipy import signal
from scipy.io import wavfile
import matplotlib.pyplot as plt


sample_rate, data = wavfile.read("workshop/spectogram/radio.wav")


if len(data.shape) == 2:
    data = np.mean(data, axis=1)


data = data / np.max(np.abs(data), axis=0)


duration = 20 # in seconds
data = data[:duration * sample_rate]

nperseg = int(sample_rate*0.1) #this can vary

f, t, Sxx = signal.spectrogram(data, sample_rate,nperseg=nperseg)


Sxx_log = np.log(Sxx + 1e-10) 


plt.figure(figsize=(10, 6))
plt.pcolormesh(t, f, Sxx_log, shading='ground') 
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.ylim(0,5000)
plt.title('Spectrogram of the Audio Signal (First duration seconds)')
plt.colorbar(label='Log Power Spectrum [dB]')
plt.show()

