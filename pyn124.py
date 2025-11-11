#I reffered from chatgpt and i understood the logic then i proceeded the program with my own 
import numpy as np
from scipy.fftpack import fft, ifft
t=np.linspace(0,1,500) 
signal=np.sin(2*np.pi*5*t)+0.5*np.sin(2*np.pi*20*t)
fft_signal=fft(signal)
freq=np.fft.fftfreq(len(t),d=t[1]-t[0])
print("Frequencies (first 10):")
print(freq[:10])
print("\nFFT Values (first 10):")
print(fft_signal[:10])
reconstructed =ifft(fft_signal)
print("\nReconstructed Signal (first 10 samples):")
print(reconstructed[:10].real)
