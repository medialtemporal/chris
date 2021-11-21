# Code from https://klyshko.github.io/teaching/2019-02-22-teaching 

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

def analyseData(sampfreqinput1, soundfileinput ):
  sampFreq=sampfreqinput1
  sound=soundfileinput

  sound = sound / 2.0**15

  sound.shape

  length_in_s = sound.shape[0] / sampFreq

  signal = sound[:,0]

  fft_spectrum = np.fft.rfft(signal)
  freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
  fft_spectrum_abs = np.abs(fft_spectrum)

  listtopass = []

  for i,f in enumerate(fft_spectrum_abs):
    #print(i)
    if f > 0.0000003: #only works at 60 BPM???
      listtopass.append(freq[i])
  return listtopass
