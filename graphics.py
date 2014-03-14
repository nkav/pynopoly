from termcolor import cprint, colored
import sys

def newscreen():
  print '\n' * 22

def propertiesowned(properties):
  places = sum(properties.values(), [])
  coloredplaces = []
  for place in places:
    if place.bg:
      coloredplaces.append(colored(place.name, place.text, place.bg))
    else:
      coloredplaces.append(colored(place.name, place.text))
  if places:
    print "You own the following properties: " + ", ".join(coloredplaces) + "."
  else:
    print "You don't own any properties yet."

def printboard():
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
  cprint(u"\u2588", 'blue', end='\n\n')

def printplayer(symbol, position):
  sys.stdout.write(" "*(position)*2 + symbol + '\n')
