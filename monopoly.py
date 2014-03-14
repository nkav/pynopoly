from graphics import newscreen
from board import board
from player import Player

class Monopoly:
  players = []
  turns = 10  
 
  def __init__(self, players, turns):
    self.players = players
    self.turns = turns

  def nextturn(self):
    for player in self.players:
      if (not player.bankrupt):
        if(not player.servetime()):
          print ("%s's turn." % (player))
          player.roll() 
        else:
          player.jailtimeleft()
  
  def start(self):
    for i in xrange(self.turns):
      newscreen()
      print "Now starting turn %d." % (i)
      self.nextturn()

if __name__ == '__main__':
  main = Player("Nilesh", simulate=True) 
  player2 = Player("New Player", simulate=True) 
  newgame = Monopoly([main, player2], 100)
  newgame.start()
