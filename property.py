#!/usr/bin/env python
""" 
property.py - the basic class for a Property, as well as for the RailroadProperty
"""

# TODO: implement correct utility property rent, mortgaging

class Property:
  name = ""
  price = 0 
  owner = None 
  rent = 0 
  group = ''
  text = 'white'
  bg = None
  houses = 0
  
  #number of total available properties for each group type
  available = {
    'railroads': 4,
    'utilities': 2,
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

  def add_house(self):
    self.houses += 1

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
