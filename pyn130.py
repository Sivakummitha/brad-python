import numpy as np
from scipy import signal
fs=500
t=np.linspace(0,1,fs,endpoint=False)
sig=np.sin(2*np.pi*5*t)+0.5*np.random.randn(t.size)
print("Generated noisy signal (first 10 values):",sig[:10])
b,a=signal.butter(4,0.1)
filtered=signal.filtfilt(b,a,sig)
print("Filtered signal (first 10 values):",filtered[:10])
peaks,_=signal.find_peaks(filtered)
print("Number of peaks found:",len(peaks))
print("Peak indices (first 10):",peaks[:10])
