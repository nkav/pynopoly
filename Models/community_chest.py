from space import Space
from random import shuffle
from cards import community_chest

class CommunityChest(Space):

  def __init__(self):
    self.cards = list(community_chest)
    shuffle(self.cards)
    self.community_index = 0
    self.symbol = "!"
    self.group = 'default'


  def handle_land(self, player, roll, ui):
    ui.print_message("You landed on Community Chest!")
    if not player.simulate:
      ui.raw_input("Enter to draw a card. ")
    self.cards[self.community_index](player, ui)
    self.community_index += 1
    self.community_index %= len(self.cards)