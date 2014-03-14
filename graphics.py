#!/usr/bin/env python
""" 
graphics.py - functions for the primitive terminal interface.
"""

from termcolor import cprint, colored
import os,sys

def newscreen():
  #clears screen
  os.system('cls' if os.name == 'nt' else 'clear')

def sectionbreak():
  #logical breaks between sections so text is not distracting
  print '*' * 70


def propertiesowned(player):
  #Prints all the properties the user owns and colors them appropriately.
  places = sum(player.owned.values(), [])
  coloredplaces = []
  for place in places:
    if place.bg:
      coloredplaces.append(colored(place.name, place.text, place.bg))
    else:
      coloredplaces.append(colored(place.name, place.text))
  if places:
    print "%s owns the following properties: " % (player) + ", ".join(coloredplaces) + "."
  else:
    print "%s doesn't own any properties yet." % (player)

def printboard():
  # A linear rendition of the board with each space colored appropriately.
  cprint (u"G", 'green', 'on_yellow', end= ' ') 
  cprint(u"\u2588", 'blue', 'on_red', end=' ')
  print u"C ", 
  cprint(u"\u2588", 'blue', 'on_red', end='')
  print u"\u2588", 
  print u"R ", 
  cprint(u"\u2588", 'blue', 'on_white', end='')
  print u"c ", 
  cprint(u"\u2588", 'blue', 'on_white', end=' ')
  cprint(u"\u2588", 'blue', 'on_white', end='')
  print u"j ", 
  cprint(u"\u2588", 'magenta', end='')
  print u"\u2588 ", 
  cprint(u"\u2588", 'magenta', end=' ')
  cprint(u"\u2588", 'magenta', end='')
  print u"R ", 
  cprint(u"\u2588", 'red', 'on_yellow', end='')
  print u"C ", 
  cprint(u"\u2588", 'red', 'on_yellow', end=' ')
  cprint(u"\u2588", 'red', 'on_yellow', end='')
  print u"F ", 
  cprint(u"\u2588", 'red', end='')
  print u"C ", 
  cprint(u"\u2588", 'red', end=' ')
  cprint(u"\u2588", 'red', end='')
  print u"R ", 
  cprint(u"\u2588", 'yellow', end=' ')
  cprint(u"\u2588", 'yellow', end='')
  print u"\u2588 ", 
  cprint(u"\u2588", 'yellow', end='')
  print u"J ", 
  cprint(u"\u2588", 'green', end=' ')
  cprint(u"\u2588", 'green', end='')
  print u"C ", 
  cprint(u"\u2588", 'green', end='')
  print u"R",
  print u"c ", 
  cprint(u"\u2588", 'blue', end='')
  print u"\u2588 ", 
  cprint(u"\u2588", 'blue', end='\n')

def printplayer(symbol, position):
  # Prints the players location on the board according to printboard()
  sys.stdout.write(" "*(position)*2 + symbol + '\n')
