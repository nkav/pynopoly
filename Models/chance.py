from space import Space
from random import shuffle
from cards import chance

class Chance(Space):

  def __init__(self):
    self.cards = list(chance)
    shuffle(self.cards)
    self.chance_index = 0
    self.symbol = "?"
    self.group = 'default'

  def handle_land(self, player, roll, ui):
    ui.print_message("You landed on Chance!")
    if not player.simulate:
      ui.raw_input("Enter to draw a card. ")
    self.cards[self.chance_index](player, ui)
    self.chance_index += 1
    self.chance_index %= len(self.cards)