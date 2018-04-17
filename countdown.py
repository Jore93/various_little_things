# -*- encoding: utf-8 -*-

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

from datetime import datetime
import time 

#date2 = raw_input("Give the time you're counting in: ")
#now = datetime.now()

def count_down(seconds):
  for t in range(seconds, -1, -1):
    # format as 2 digit integers, fills with zero to the left
    # divmod() gives minutes, seconds
    mins,secs = divmod(t,60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    print(str(days)+" päivää, "+str(hours)+" tuntia, "+str(mins)+" minuuttia ja "+str(secs)+" sekuntia.")
    time.sleep(1)

def dateDiffInSeconds(date1, date2):
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds

#import tkinter as tk


def main():
#  root = tk.Tk()
#  root.title("Aikaa näkemiseen")
#  label = tk.Label(root, fg="black")
#  label.pack()
  while True:
    try:
      date2 = datetime.strptime(raw_input("Päivä johon lasketaan aikaa (d.m.Y h.m.s): "), '%d.%m.%Y %H.%M.%S')
      break
    except ValueError:
      print("Syötä aika muodossa d.m.Y h.m.s")

  now = datetime.now()

  date = dateDiffInSeconds(now, date2)
  count_down(date)

if __name__ == "__main__":
  main()
