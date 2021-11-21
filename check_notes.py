import sounddevice as sd
import eugene as eu
import scoring as sc


#fs is the sample rate (sample frequency) and my_recording is the data part of the wav file (replaces sound in eugene)

fs = 44100
freq_hz=440


def recording(e_high, g, b, d, a, e_low, duration):
  my_recording =sd.rec(int(duration * fs), samplerate=fs,   channels= 1)
  sd.wait()
  return(sc.get_frequency(e_high, g, b, d, a, e_low,(eu.analyseData(fs,my_recording))))
    








#frequencies for frets 1-20 on each string

lowerEfreq=[82.41,87.31,92.5,98,103.83,110,116.54,123.47,130.81,146.83,155.56,164.81,174.61,185,196,207.65,220,233.08,246.94]
Afreq=[110.00,116.54,123.47,130.81,138.59,146.83,155.56,164.81,174.61,185,196,207.65,220,233.08,246.94,261.63,277.18,293.66,311.13,329.63]
Dfreq=[146.83,155.56,164.81,174.61,185,196,207.65,220,233.08,246.94,261.63,277.18,293.66,311.13,329.63,349.23,369.99,392,415.3,440]
Gfreq=[196,207.65,220,233.08,246.94,261.63,277.18,293.66,311.13,329.63,349.23,369.99,392,415.3,440,466.16,493.88,523.25,554.37,587.33]
Bfreq=[246.94,261.63,277.18,293.66,311.13,329.63,349.23,369.99,392,415.3,440,466.16,493.88,523.25,554.37,587.33,622.25,659.25,698.46,739.99]
higherEfreq=[329.63,349.23,369.99,392,415.3,440,466.16,493.88,523.25,554.37,587.33,622.25,659.25,698.46,739.99,783.99,830.61,880,932.33,987.77]
