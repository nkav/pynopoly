#!/usr/bin/env python
""" 
pynopoly.py - creates and simulates a game of Monopoly 
"""

from graphics import newscreen
from board import board
from player import Player

__author__ = "Nilesh Kavthekar"
__copyright__ = "Copyright 2014, Nilesh Kavthekar"
__credits__ = ["Nilesh Kavthekar"]
__license__ = "GPL"
__version__ = "0.0.7"
__maintainer__ = "Nilesh Kavthekar"
__email__ = "nkav@wharton.upenn.edu"
__status__ = "Development"

class Monopoly:
  players = []
  turns = 10  
 
  def __init__(self, players, turns):
    self.players = players
    self.turns = turns

  def nextturn(self):
    #Plays a turn with all players, and handles if a Player is in jail/bankrupt.
    for player in self.players:
      if (not player.bankrupt):
        if(not player.servetime()):
          print ("%s's turn." % (player))
          player.roll() 
        else:
          player.jailtimeleft()
  
  def start(self):
    #For the given number of turns in a game (default 10), plays that many turns.
    for i in xrange(self.turns):
      newscreen()
      print "Now starting turn %d." % (i)
      self.nextturn()

if __name__ == '__main__':
  #Simulates a 100-turn game with two players
  main = Player("Nilesh", simulate=True) 
  player2 = Player("New Player", simulate=True) 
  newgame = Monopoly([main, player2], 100)
  newgame.start()
