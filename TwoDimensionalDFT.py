from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

#Opening Image
img = Image.open("dftraw1.png")
img_arr = np.asarray(img)
fourier = np.fft.fft2(img_arr)
fourier = np.fft.fftshift(fourier)

fourier = np.abs(fourier)

print(fourier)

fourier = fourier + 0.0000001
fourier = np.log10(fourier)

lowest = np.nanmin(fourier[np.isfinite(fourier)])
highest = np.nanmax(fourier[np.isfinite(fourier)])

original_range = highest - lowest
norm_fourier = (fourier - lowest) / original_range * 255

#print(norm_fourier)

fourier_img = Image.fromarray(norm_fourier.astype('uint8'))

print(fourier_img)

fourier_img.save('2ddft1.png')
