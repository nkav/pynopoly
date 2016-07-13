#!/usr/bin/env python
""" 
pynopoly.py - creates and simulates a game of Monopoly 
"""
import sys, getopt

from tabulate import tabulate
from graphics import new_screen, print_everything, section_break
from board import board
from Models.player import Player

__author__ = "Nilesh Kavthekar"
__copyright__ = "Copyright 2016, Nilesh Kavthekar"
__credits__ = ["Nilesh Kavthekar"]
__license__ = "GPL"
__version__ = "0.0.9"
__maintainer__ = "Nilesh Kavthekar"
__email__ = "nakavthekar@gmail.com"
__status__ = "Development"

class Pynopoly:

  def __init__(self, players, turns):
    self.players = players
    self.turns = turns

  def game_ended(self):
    bankrupt_players = sum(1 for player in self.players if player.bankrupt)
    alive_players = len(self.players) - bankrupt_players
    if alive_players == 1:
      return True
    else:
      return False

  def next_turn(self):
    #Plays a turn with all players, and handles if a Player is in jail/bankrupt.
    for player in self.players:
      if player.bankrupt:
        continue
      if self.game_ended():
        break

      if player.in_jail():
        player.serve_time()
      else:
        print ("%s's turn." % (player))
        print_everything(self.players, board)
        player.roll() 

  def start(self):
    #For the given number of turns in a game (default 10), plays that many turns.
    for i in xrange(self.turns):
      new_screen()
      print "Now starting turn %d." % (i)
      self.next_turn()
      if self.game_ended():
        break

    # Game over!
    self.print_rankings()

    

  def print_rankings(self):
    print "Game Over!"
    finishing_order = sorted(self.players, key=lambda player: player.total_assets(), reverse=True)
    winner = finishing_order[0]
    print "The winner was %s with $%d in assets." % (winner, winner.total_assets())
    section_break()
    print "STANDINGS:"
    headers = ["Name", "Assets", "Bankrupt"]
    boolean_to_english = lambda x: "Yes" if x else "No"
    standings = [[player.name, player.total_assets(), boolean_to_english(player.bankrupt)] for player in finishing_order]
    print tabulate(standings, headers, tablefmt="simple")


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
    newgame = Pynopoly(players, num_turns)
    newgame.start()