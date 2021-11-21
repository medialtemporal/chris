import time
import check_notes as cn
def printstuff(a,b,c,d,e,f,bpm):
  #print stuff from input strings a-f. Prints horizontally, using the bpm value to specify how fast it prints
  correctnotes = 0
  wrongnotes = 0
  waythrough = 0
  length = len(a)
  timepernote=60/(2*bpm)

  previous = -1
  a2=[]
  for item in a:
    if(item!= ' ' and item != '|'):
      if (item == '-'):
        a2.append(-1)
      elif(item == '>'):
        a2.append(previous)
      else:
        a2.append(int(item))
        previous = int(item)
    else:
      a2.append(-1)


  b2=[]
  for item in b:
    if(item!= ' ' and item != '|'):
      if (item == '-'):
        b2.append(-1)
      elif(item == '>'):
        b2.append(previous)
      else:
        b2.append(int(item))
        previous = int(item)
  else:
      b2.append(-1)

  c2=[]
  for item in c:
    if(item!= ' ' and item != '|'):
      if (item == '-'):
        c2.append(-1)
      elif(item == '>'):
        c2.append(previous)
      else:
        c2.append(int(item))
        previous = int(item)
    else:
      c2.append(-1)

  d2=[]
  for item in d:
    if(item!= ' ' and item != '|'):
      if (item == '-'):
        d2.append(-1)
      elif(item == '>'):
        d2.append(previous)
      else:
        d2.append(int(item))
        previous = int(item)
    else:
      d2.append(-1)

  e2=[]
  for item in e:
    if(item!= ' ' and item != '|'):
      if (item == '-'):
        e2.append(-1)
      elif(item == '>'):
        e2.append(previous)
      else:
        e2.append(int(item))
        previous = int(item)
    else:
      e2.append(-1)

  f2=[]
  for item in f:
    if(item!= ' ' and item != '|'):
      if (item == '-'):
        f2.append(-1)
      elif(item == '>'):
        f2.append(-1)
      else:
        f2.append(int(item))
        previous = int(item)
    else:
      f2.append(-1)

  while(waythrough+39<length):
    if(a[waythrough]=='|' or a[waythrough]==' ' ):
      waythrough+=1
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(a[waythrough:waythrough + 39])
    print(b[waythrough:waythrough + 39])
    print(c[waythrough:waythrough + 39])
    print(d[waythrough:waythrough+39])
    print(e[waythrough:waythrough + 39])
    print(f[waythrough:waythrough + 39])



    if(cn.recording(a2[waythrough],b2[waythrough],c2[waythrough],d2[waythrough],e2[waythrough],f2[waythrough],timepernote)):
      correctnotes+=1
    else:
      wrongnotes+=1

    time.sleep(timepernote) #replace the sleep here with logic related to recording the sound and saving it/processing it
    waythrough+=1

  print("Score: ", (float(correctnotes)/(float(correctnotes + wrongnotes))))
























#here onward is currently redundant
def printstuff2(a,bpm):
    #prints stuff from input list a. Prints vertically, using the bpm value to specify how fast it prints
    waythrough=0
    length=len(a)
    timepernote=60/bpm
    while(waythrough+24<44):
        temp=""
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        for x in range(24):
            temp+="\n"+a[waythrough+24-x]
        print(temp)
        time.sleep(timepernote)
        waythrough+=1

def getLongArrayFromString(a,b,c,d,e,f):
  #getArrayFromStrings but it also makes the stuff longer so it doesn't instantly end
  for x in range(3):
    a+=a
    b+=b
    c+=c
    d+=d
    e+=e
    f+=f
  return getArrayFromStrings(a,b,c,d,e,f)

def getArrayFromStrings(a, b, c, d, e, f):
    #This code takes the 6 strings as input, and makes them all into a list, where each element is one line for the output. It also deletes all of the filler lines(lines with only spaces, or vertical bars), and changes all "-" to " " to improve readability
    list = []
    for x in range(len(a)):
        if(a[x]!='|' and a[x]!=' '):
            list.append((a[x]+"|"+b[x]+"|"+c[x]+"|"+d[x]+"|"+e[x]+"|"+f[x]).replace('-',' ').replace('>','^'))

    return list

"""
#old testing stuff (older version of getArrayFromStrings)
list = []
input = "0>>> 3--- 5--- ----|0--- 3--- 6-5- ----"
for x in range(4):
    for y in input:
        list.append(" | | | |"+y)
printstuff2(list,60)
"""
