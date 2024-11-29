import numpy as np
import matplotlib.pyplot as plt

# Sampling settings
Fs = 100  
N = 1000  
t = np.linspace(-10, 10, N)  


y1 = 1 + np.cos(4 * t + 2 * np.abs(t))

y2 = 1 + np.cos(-4 * t + 2 * np.abs(t))


y1_fft = np.fft.fftshift(np.fft.fft(y1))
y2_fft = np.fft.fftshift(np.fft.fft(y2))


y1_mag = np.abs(y1_fft)
y2_mag = np.abs(y2_fft)


f = np.linspace(-Fs/2, Fs/2, N)

#----------------------------------------------------------------------------------------------



plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plt.plot(t, y1, label='y1 = 1 + cos(4x + 2|x|)')
plt.title('y1: Original Signal')
plt.xlabel('time')
plt.ylabel('y1')
plt.grid()
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(t, y2, label='y2 = 1 + cos(-4x + 2|x|)', color='orange')
plt.title('y2: Original Signal')
plt.xlabel('time')
plt.ylabel('y2')
plt.grid()
plt.legend()

# Plot the FFT magnitude
plt.subplot(4, 1, 3)
plt.plot(f, y1_mag, label='FFT of y1')
plt.title('FFT of y1')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid()
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(f, y2_mag, label='FFT of y2', color='orange')
plt.title('FFT of y2')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()



plt.figure(figsize=(12, 2))
plt.text(0.5, 0.5,
         "The FFT of y1 and y2 are identical in magnitude,\n"
         "demonstrating that the frequency components are independent\n"
         "of their order in the time domain.",
         fontsize=12, ha='center', va='center')
plt.axis('off')  
plt.show()