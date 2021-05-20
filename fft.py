import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt
#adoped from https://github.com/Metallicode/RandomProjects_IOT/blob/master/06_fft_analysis/python_fft.py
#added loop to covert into xyz file 
#run like python fft.py > out.xyz then open in mesh lab and run commands listed in writeup 
s_rate, signal = wavfile.read("strangeFruit.wav") 

FFT = abs(scipy.fft.fft(signal))
freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate))

for i in range(len(FFT)//2):
	print(FFT[i][0], FFT[i][1], freqs[i])
#print(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)])
plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)])                                                          
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()
