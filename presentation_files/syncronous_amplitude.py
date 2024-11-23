import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
sampling_rate = 44100  # Hz
duration = 5          # seconds
window_size = 1024    # samples per chunk

# Buffer for storing audio chunks
audio_buffer = np.zeros(window_size)

# Callback to stream microphone input
def audio_callback(indata, frames, time, status):
    global audio_buffer
    audio_buffer = indata[:, 0]  # Extract single channel (mono)

# Setup sounddevice stream
stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=sampling_rate)
stream.start()

# Plotting setup
fig, ax = plt.subplots()
line, = ax.plot(audio_buffer, lw=2)
ax.set_ylim([-1, 1])
ax.set_xlim([0, window_size])
ax.set_title("Real-Time Microphone Input (Time-Domain)")
ax.set_xlabel("Sample Index")
ax.set_ylabel("Amplitude")

# Animation update function
def update(frame):
    global audio_buffer
    line.set_ydata(audio_buffer)
    return line,

ani = FuncAnimation(fig, update, interval=30)
plt.show()

stream.stop()
stream.close()
