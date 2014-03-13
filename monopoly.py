from board import board
from player import Player

class Monopoly:
  players = []
  turns = 100  
 
  def __init__(self, players, turns):
    self.players = players
    self.turns = turns

  def nextturn(self):
    for player in self.players:
      if (not player.bankrupt):
        if(not player.servetime()):
          player.roll() 
  
  def start(self):
    for i in xrange(self.turns):
      print "Now starting turn %d." % (i)
      self.nextturn()



if __name__ == '__main__':
  main = Player("Main Player") 
  newgame = Monopoly([main], 100)
  newgame.start()
