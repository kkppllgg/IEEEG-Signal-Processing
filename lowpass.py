import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt


cutoff_freq = 100  
fs = 1000  
order = 1  


nyq = 0.5 * fs
normal_cutoff = cutoff_freq / nyq
b, a = butter(order, normal_cutoff, btype='highpass')


t = np.linspace(0, 1, 1000)  
data = np.sin(2*np.pi*50*t) 


filtered_data = filtfilt(b, a, data)


plt.figure(figsize=(10, 6))

plt.plot(t, data, label='Original Signal 50Hz')
plt.plot(t, filtered_data, label='Filtered Signal')

plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('High-Pass Filtering Example (fc=100Hz)')
plt.legend()
plt.grid(True)

plt.show()