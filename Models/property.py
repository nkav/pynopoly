#!/usr/bin/env python
""" 
property.py - the basic class for a Property, as well as for the RailroadProperty
"""

from space import Space

# TODO: implement correct utility property rent, mortgaging

class Property(Space):
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

  def __init__(self, data):
    self.name = data['name']
    self.price = data['price']
    self.group = data['group']
    self.owner = None 
    self.houses = 0
    self.rent = data['rent'] 

  def __repr__(self):
    return self.name

  def handle_land(self, player, roll):
    print "Landed on %s." % (self)
    player.rent_or_buy(self)

  def add_house(self):
    if (self.houses < 5): 
      self.owner.pay(100, None)
      self.houses += 1
      print "You just bought a house on %s!" % self.name 
    else:
      print "You already have 5 houses on %s!" % self.name
    

  def get_rent(self):
    """Charges rent depending on monopoly.
      If owner owns all properties of a given color, he/she is able to charge twice the rent.
    """ 
    
    if self.owner.is_monopoly(self.group) and not self.houses:
      # special case if there is an undeveloped monopoly
      return self.rent[0]*2
    else:
      return self.rent[self.houses]  

  def purchased(self, person):
    """Allows a given Player to purchase a card."""
    self.owner = person

  def sold(self):
    """Allows a given Player to sell the card back to the Bank."""
    self.owner = None 
  
class RailroadProperty(Property):

  def __init__(self, name):
    self.name = name
    self.price = 200
    self.group = 'railroads'
    self.owner = None
    self.rent = {
      1: 25,
      2: 50,
      3: 100,
      4: 200
    }

  def get_rent(self):
    if self.owner:
      return self.rent[len(self.owner.owned_by_group['railroads'])]
    else:
      return self.rent[1]
