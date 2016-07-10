#!/usr/bin/env python
""" 
pynopoly.py - creates and simulates a game of Monopoly 
"""
import sys, getopt

from graphics import new_screen, print_everything
from board import board
from player import Player

__author__ = "Nilesh Kavthekar"
__copyright__ = "Copyright 2016, Nilesh Kavthekar"
__credits__ = ["Nilesh Kavthekar"]
__license__ = "GPL"
__version__ = "0.0.8"
__maintainer__ = "Nilesh Kavthekar"
__email__ = "nakavthekar@gmail.com"
__status__ = "Development"

class Monopoly:
  players = []
  turns = 10  
 
  def __init__(self, players, turns):
    self.players = players
    self.turns = turns

  def next_turn(self):
    #Plays a turn with all players, and handles if a Player is in jail/bankrupt.
    for player in self.players:
      if player.bankrupt:
        continue
      if not player.servetime():
        print ("%s's turn." % (player))
        print_everything(self.players)
        player.roll() 
      else:
        player.jail_time_left()
  
  def start(self):
    #For the given number of turns in a game (default 10), plays that many turns.
    for i in xrange(self.turns):
      new_screen()
      print "Now starting turn %d." % (i)
      self.next_turn()




if __name__ == '__main__':
  name = "Main Player"
  num_cpus = 1
  num_turns = 10
  simulate = False
  try:
    opts, args = getopt.getopt(sys.argv[1:],"hsu:c:t:",["username=", "cpus=","turns="])
  except getopt.GetoptError:
    print 'pynopoly.py [-s] [-u <username>] [-c <number of CPUs>] [-t <number of turns>]'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'pynopoly.py [-s] [-u <username>] [-c <number of CPUs>] [-t <number of turns>]'
      sys.exit()
    elif opt in ("-s", "--simulate"):
      simulate = True
    elif opt in ("-u", "--username"):
      name = arg
    elif opt in ("-c", "--cpus"):
      num_cpus = int(arg)
    elif opt in ("-t", "--turns"):
      num_turns = int(arg)

  players = [Player(name, simulate=simulate)]
  if num_cpus >= 1 and num_cpus <= 5:
    for cpu_num in xrange(num_cpus):
      cpu_name = "player" + str(cpu_num)
      players.append(Player(cpu_name, simulate=True))
    newgame = Monopoly(players, num_turns)
    newgame.start()