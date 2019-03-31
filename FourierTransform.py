import numpy as np
import matplotlib.pyplot as plt

#Beginning Example

#Number of Sample Points
N = 100
#Signal Work
signal = np.r_[0 : 10 * N : 10]
signal_sin = np.sin(signal)
signal_fft = np.fft.fft(signal_sin)
signal_fft_pow = np.abs(signal_fft)
#Signal Plot Points
plt.plot(signal_sin, '-o', markersize = 2)
plt.savefig('FFTOriginal1.png')

plt.clf()

plt.plot(signal_fft_pow, '-o', markersize = 2)
plt.savefig('FFTResult1.png')

plt.clf()
