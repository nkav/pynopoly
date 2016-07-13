#!/usr/bin/env python
""" 
property.py - the basic class for a Property, as well as for the RailroadProperty
"""

from space import Space
from probability import die

# TODO: implement correct utility property rent, mortgaging

class Ownable(Space):

  def __repr__(self):
    return self.name

  def mortgageable():
    return self.houses == 0

  def mortgage():
    self.mortgaged = True

  def unmortgage():
    self.mortgaged = False

  def mortgage_value():
    return self.price / 2

  def price_to_unmortgage():
    return mortgage_value * 1.1

  def purchase(self, person):
    """Allows a given Player to purchase a card."""
    self.owner = person

  def handle_land(self, player, roll, ui):
    ui.print_message("Landed on %s." % (self))
    self.rent_or_buy(player, roll, ui)

  def sell(self):
    """Allows a given Player to sell the card back to the Bank."""
    self.owner = None 

  def rent_or_buy(self, player, roll, ui):
    """Checks if a property is owned, and then either pays rent or buys."""
    if self.owner == player:
      ui.print_message("%s already owns %s!" % (player, self))
    elif self.owner: 
      ui.print_message("This property is already owned by by %s. %s must pay rent." % (self.owner, player))
      self.charge_rent(player, roll, ui)
    else:
      player.buy(self)

  def charge_rent(self, player, roll, ui):
    if not self.mortgaged:
      rent = self.get_rent(roll, ui)
      player.pay(rent, self.owner) # force user to either pay or bankrupt
    else:
      ui.print_message("%s is mortgaged! %s owes no rent." (self, player))


class Utility(Ownable):
  def __init__(self, data):
    self.name = data['name']
    self.price = data['price']
    self.group = data['group']
    self.owner = None 
    self.symbol = "U"
    self.mortgaged = False

  def get_rent(self, roll, ui):
    if roll is None:
      "Enter to roll dice:"
      die1 = die()
      die2 = die()
      roll = die1 + die2 
      ui.print_message("%s rolled a %d and %d to get %d." % (self, die1, die2, roll))
    if len(self.owner.owned_by_group['utilities']) == 2:
      ui.print_message("%s ownes two utilities, so rent is 10x the roll, or $%d!" % (self, roll*11))
      return roll * 11
    else:
      ui.print_message("%s ownes one utility, so rent is 4x the roll, or $%d!" % (self, roll*4))
      return roll * 4


class Property(Ownable):
  #number of total available properties for each group type
  available = {
    'purples': 2,
    'lightblues': 3,
    'magentas': 3,
    'oranges': 3, 
    'reds': 3,
    'yellows': 3,
    'greens': 3,
    'blues': 2 
  }

  house_prices = {
    'purples': 50,
    'lightblues': 50,
    'magentas': 100,
    'oranges': 100, 
    'reds': 150,
    'yellows': 150,
    'greens': 200,
    'blues': 200 
  }

  def __init__(self, data):
    self.name = data['name']
    self.price = data['price']
    self.group = data['group']
    self.owner = None 
    self.houses = 0
    self.rent = data['rent'] 
    self.mortgaged = False

  def label(self):
    return u"\u2612" if self.owner else u"\u2610"


  def house_price(self):
    return Property.house_prices[self.group]

  def add_house(self):
    self.houses + 1
    
  def remove_house(self):
    self.houses -= 1  

  def get_rent(self, roll, ui):
    """Charges rent depending on monopoly.
      If owner owns all properties of a given color, he/she is able to charge twice the rent.
    """ 
    if self.owner.is_monopoly(self.group) and not self.houses:
      # special case if there is an undeveloped monopoly
      return self.rent[0]*2
    else:
      return self.rent[self.houses]  
  
class RailroadProperty(Ownable):

  def __init__(self, name):
    self.name = name
    self.price = 200
    self.group = 'railroads'
    self.owner = None
    self.mortgaged = False
    self.symbol = "R"
    self.rent = {
      1: 25,
      2: 50,
      3: 100,
      4: 200
    }

  def get_rent(self, roll, ui):
    if self.owner:
      return self.rent[len(self.owner.owned_by_group['railroads'])]
    else:
      return self.rent[1]
