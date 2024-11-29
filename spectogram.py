from asyncio.windows_events import NULL
import numpy as np
from scipy import signal
from scipy.io import wavfile
import matplotlib.pyplot as plt


sample_rate, data = wavfile.read("workshop/spectogram/updown.wav")


if len(data.shape) == 2:
    data = np.mean(data, axis=1)



data = data / np.max(np.abs(data), axis=0)#####

nperseg = int(sample_rate*0.1)#####


f, t, Sxx = signal.spectrogram(data, sample_rate,nperseg=nperseg,window=np.hanning(nperseg))


plt.figure(figsize=(10, 6))
plt.pcolormesh(t, f, np.log(Sxx), shading='gouraud')  # log scale for better visualization
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.title('Spectrogram of the Audio Signal')
plt.colorbar(label='Log Power Spectrum [dB]')
plt.show()
