from termcolor import cprint
import sys

def printboard():
  cprint (u"G", 'green', 'on_yellow', end= ' ') 
  cprint(u"\u2588", 'blue', 'on_red', end=' ')
  print u"C ", 
  cprint(u"\u2588", 'blue', 'on_red', end='')
  print u"\u2588", 
  print u"R ", 
  cprint(u"\u2588", 'blue', 'on_grey', end='')
  print u"c ", 
  cprint(u"\u2588", 'blue', 'on_grey', end=' ')
  cprint(u"\u2588", 'blue', 'on_grey', end='')
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
