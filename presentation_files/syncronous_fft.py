from matplotlib.animation import FuncAnimation
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

def low_pass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return lfilter(b, a, data)

# Parameters
sampling_rate = 1* 44100  # Hz
window_size = 1024    # samples per chunk

# Initialize audio buffer
audio_buffer = np.zeros(window_size)

# Audio callback to capture microphone data
def audio_callback(indata, frames, time, status):
    global audio_buffer
    audio_buffer = indata[:, 0]  # Mono channel data

# Start the microphone stream
stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=sampling_rate)
stream.start()

# Plot setup
fig, ax = plt.subplots()
freqs = np.fft.fftfreq(window_size, 1 / sampling_rate)[:window_size // 2]  # Frequency bins
line, = ax.plot(freqs, np.zeros_like(freqs), lw=2)  # Initial plot with zeroed data
ax.set_xlim(0, sampling_rate // 2)  # Positive frequencies only
ax.set_ylim(-100, 0)  # dB scale for magnitude
ax.set_title("Real-Time FFT (Frequency-Domain)")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Magnitude (dB)")

# Update function for animation
def update(frame):
    global audio_buffer
    filtered_data = low_pass_filter(audio_buffer, 1500, sampling_rate)
    fft_data = np.fft.fft(audio_buffer)  # Compute FFT
    magnitude = np.abs(fft_data[:window_size // 2])  # Positive frequency magnitudes
    magnitude_db = 20 * np.log10(magnitude + 1e-6)  # Avoid log(0) with small constant
    line.set_ydata(magnitude_db)  # Update magnitude data
    return line,

# Create animation
ani = FuncAnimation(fig, update, interval=30)
plt.show()

# Stop and close the stream
stream.stop()
stream.close()
