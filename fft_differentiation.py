import matplotlib.pyplot as plt
import numpy as np

def mag_fft_mine(Freq, Sampl, starting):
    # fft plot function sampling freq, samples, when to start
    T = Sampl / Freq  # for how much time
    t = np.linspace(starting, T + starting, Sampl, endpoint=False)  
    
    s = np.piecewise(
        t,
        [t < 4 * np.pi, t >= 4 * np.pi],
        [lambda t: np.cos(2 * np.pi * t), lambda t: np.cos(4 * np.pi * t)],
    )
    plt.figure(1) 
    plt.plot(t, s)
    plt.title("Signal in time domain")
    plt.xlabel("Time(s)")
    plt.ylabel("Voltage(V)")

    s = s * np.hamming(Sampl)  
    S = np.fft.fftshift(np.fft.fft(s)) 
    f = np.linspace(-Freq / 2, Freq / 2, Sampl, endpoint=False) 
    S_mag = np.abs(S)  

    plt.figure(2) 
    plt.plot(f, S_mag)
    plt.title("Signal in frequency domain")
    plt.xlabel("Frequency(Hz)")
    plt.ylabel("Magnitude")
    plt.tight_layout()
    plt.show()


mag_fft_mine(30, 750, 0)       # all of the signal (125/5 = 25 seconds)
mag_fft_mine(30, 375, 0)       # the first part (low frequency) (12.5 seconds from 0 seconds)
mag_fft_mine(30, 375, 12.5)    # the second part (high frequency (12.5 seconds from 25 seconds)
