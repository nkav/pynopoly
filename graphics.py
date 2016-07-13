#!/usr/bin/env python
""" 
graphics.py - functions for the primitive terminal interface.
"""
from Models.property import Property, RailroadProperty
from termcolor import cprint, colored
import os,sys

def new_screen():
  #clears screen
  os.system('cls' if os.name == 'nt' else 'clear')

def section_break():
  #logical breaks between sections so text is not distracting
  print '*' * 70


group_colors = {
  'purples': 
    {
      'text': 'blue',
      'bg': 'on_red'
    }, 
  'lightblues': 
    {
      'text': 'blue', 
      'bg': 'on_white'
    },
  'magentas': 
    {
      'text': 'magenta'
    },
  'oranges': 
    {
      'text': 'red',
      'bg': 'on_yellow'
    },
  'reds': 
    {
      'text': 'red'
    },
  'yellows': 
    {
      'text': 'yellow'
    },
  'greens': 
    {
      'text': 'green'
    },
  'blues': 
    {
      'text': 'blue'
    },
  'railroads': 
    {
      'text': 'white'
    },
  'utilities': 
    {
      'text': 'white'
    }
}


def properties_owned(player):
  #Prints all the properties the user owns and colors them appropriately.
  colored_places = []

  for group, properties in player.owned_by_group.iteritems():
    group_color = group_colors[group]
    if 'bg' in group_color:
      for place in properties:
        colored_places.append(colored(place.name, group_color['text'], group_color['bg']))
    else:
      for place in properties:
        colored_places.append(colored(place.name, group_color['text']))
  if colored_places:
    print "%s owns the following properties: " % (player) + ", ".join(colored_places) + "."
  else:
    print "%s doesn't own any properties yet." % (player)



def print_board():
  # A linear rendering of the board with each space colored appropriately.
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

def print_developments(properties):
  developments = " " * 79 
  for position in properties:
    property = properties[position]
    if type(property) is Property:
      developments = developments[:position*2-1] + str(property.houses) + developments[(position*2):]
    elif type(property) is RailroadProperty:
      developments = developments[:position*2-1] + "O" + developments[(position*2):]
        
  print developments


def print_everything(players, properties):
  print_board()
  print_developments(properties)
  for player in players:
    print_player(player.name, player.position)

def print_player(name, position):
  # Prints the players location on the board according to print_board()
  sys.stdout.write(" "*((position)*2) + "^ " + name + '\n')
