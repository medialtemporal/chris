#frequencies for frets 1-20 on each string
# 1 represents an open string
numberofchecks=0
numberofcorrect=0

def get_frequency(e_high, g, b, d, a, e_low, actualfrequencies):
  expectedFrequencies = []
  correct = True

  if not (e_high == -1 and g == -1 and b == -1 and d == -1 and a == -1 and e_low == -1):
    if (e_high != -1):
      expectedFrequencies.append(higherEfreq[e_high])
    if(g!=-1):
      expectedFrequencies.append(Gfreq[g])
    if(b!=-1):
      expectedFrequencies.append(Bfreq[b])
    if(d!=-1):
      expectedFrequencies.append(Dfreq[d])
    if(a!=-1):
      expectedFrequencies.append(Afreq[a])
    if(e_low!=-1):
      expectedFrequencies.append(lowerEfreq[e_low])

  for item in expectedFrequencies:
    isthere = False
    for otheritem in actualfrequencies:
      if  (otheritem > item * 0.95 and otheritem < item * 1.05):
        isthere = True
    correct = (isthere and correct)
  return correct

# check each line (string)
# check first character being printed for each line

# try type(int), if succeeds pass int, if not then check other stuff
# if it's - then nothing going on here, if > then it's continue/same


lowerEfreq=[82.41,87.31,92.5,98,103.83,110,116.54,123.47,130.81,146.83,155.56,164.81,174.61,185,196,207.65,220,233.08,246.94]

Afreq=[110,116.54,123.47,130.81,138.59,146.83,155.56,164.81,174.61,185,196,207.65,220,233.08,246.94,261.63,277.18,293.66,311.13,329.63]

Dfreq=[146.83,155.56,164.81,174.61,185,196,207.65,220,233.08,246.94,261.63,277.18,293.66,311.13,329.63,349.23,369.99,392,415.3,440]

Gfreq=[196,207.65,220,233.08,246.94,261.63,277.18,293.66,311.13,329.63,349.23,369.99,392,415.3,440,466.16,493.88,523.25,554.37,587.33]

Bfreq=[246.94,261.63,277.18,293.66,311.13,329.63,349.23,369.99,392,415.3,440,466.16,493.88,523.25,554.37,587.33,622.25,659.25,698.46,739.99]

higherEfreq=[329.63,349.23,369.99,392,415.3,440,466.16,493.88,523.25,554.37,587.33,622.25,659.25,698.46,739.99,783.99,830.61,880,932.33,987.77]
