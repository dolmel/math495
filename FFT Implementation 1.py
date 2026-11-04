import math
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def fft(x):
    n = len(x)
    if n == 1:
        return x # Indices go to 0 in sum, trivial case
    E = fft(x[0::2])
    O = fft(x[1::2])
    X = [np.exp(-2j * np.pi * k / n) * O[k] for k in range(n // 2)]
    return [E[k] + X[k] for k in range(n // 2)] + [E[k] - X[k] for k in range(n // 2)]

# Sample wave
fs = 2**10 # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # Period
f1 = 5    # Frequency of the wave in Hz
f2 = 25
f3 = 100

wave = (np.sin(2 * np.pi * f1 * t) 
        + 0.9 * np.cos(2 * np.pi * f2 * t)
        + 0.3 * np.sin(2 * np.pi * f3 * t)
        + 0.1 * np.random.normal(size=fs)) 

fft_result = np.array(fft(wave))

N = len(wave)
freqs = np.arange(N) * fs / N
half_n = N // 2

plt.figure(figsize=(12, 4)) # Plot original wave in time domain
plt.plot(t, wave)
plt.title('Original Wave - Time Domain')
plt.xlabel('Time, s')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()

plt.figure(figsize=(12, 4)) # Plot xfmn in frequency domain
plt.plot(freqs[:half_n], np.abs(fft_result[:half_n]) * 2 / N)
plt.title('FFT - Frequency Domain')
plt.xlabel('Frequency, Hz')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()

plt.show()