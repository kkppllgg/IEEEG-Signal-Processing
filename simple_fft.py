import numpy as np
import matplotlib.pyplot as plt


Fs = 1
N = 200

t = np.arange(N)
s = np.sin(0.15*2*np.pi*t)
s = s * np.hamming(N)
S = np.fft.fftshift(np.fft.fft(s))

S_mag = np.abs(S)

f = np.arange(Fs/-2,Fs/2,Fs/N)
plt.subplot(2,1,1)
plt.plot(f,S_mag,'.-')

plt.subplot(2,1,2)
plt.plot(t,s)

plt.show()