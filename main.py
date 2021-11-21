# Characteristically Heroic Re-Creation In Sound (C.H.R.I.S.)

# File Imports
import matas_file as mf
# import eugene as eu

def main():
  done = False
  while not done:
    # INTRO (at the beginning):
    e_high, b, g, d, a, e_low, tempo = set_up()

    # MIDDLE STUFF (using rachel, matas, adrian work)
    mf.printstuff(e_high, b, g, d, a, e_low, tempo)

    # SCORING (at the end):

    # ENDING (asks if want to play again):
    print("")
    done = play_again()

# HELPER FUNCTIONS

def set_up():
  # welcome message
  print('\nHi! Welcome to C.H.R.I.S.\n\n')

  # select song (import song file, .txt)
  song_selection = check_song()
  print('')

  # creating the tab strings
  e_high, b, g, d, a, e_low = make_strings(song_selection)

  # choose a tempo (bpm)
  tempo = get_tempo()
  print('')

  # returns 6 strings (1 for each guitar string, 1 line in the file) + an integer bpm
  return e_high, b, g, d, a, e_low, tempo


def check_song():
  selected = False
  while not selected:
    try:
      song_selection = input('Please type the name of the song you would like to play: \n').lower() + '.txt'
      tab = open(song_selection, "r")
      tab.close()
      if " " in song_selection:
        print("Please enter a name without spaces. If the name is multiple words long, please use underscores.\n")
      else:
        selected = True
    except FileNotFoundError:
      print("That file doesn't exist. Please try again.\n")
  return song_selection


def make_strings(song_selection):
  tab = open(song_selection, "r")
  e_high = tab.readline().strip()
  b = tab.readline().strip()
  g = tab.readline().strip()
  d = tab.readline().strip()
  a = tab.readline().strip()
  e_low = tab.readline().strip()
  tab.close()
  return e_high, b, g, d, a, e_low


def get_tempo():
  tempo_set = False
  while not tempo_set:
    try:
      tempo_selection = int(input('Please enter a BPM for your song: '))
      if 0 < tempo_selection < 1000:
        tempo_set = True
      else:
        print("Please enter a BPM value between 1 and 999.\n")
    except ValueError:
      print('Please enter an integer value for BPM.\n')
  return tempo_selection


def play_again():
  decided = False
  while not decided:
    selection = input("Would you like to practice another song? Please enter 'y' for 'yes', or 'n' for 'no': ")
    again = selection.lower()
    if again != 'y' and again != 'n':
      print("Please enter either 'y' or 'n'.\n")
    else:
      decided = True
  done = 0
  if again == 'y':
    done = False
  else:
    done = True
  return done


if __name__ == '__main__':
  main()
