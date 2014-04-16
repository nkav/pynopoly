#!/usr/bin/env python
""" 
property.py - the basic class for a Property, as well as for the RailroadProperty
"""

class Property:
  name = ""
  price = 0 
  owner = None 
  rent = 0 
  group = ''
  text = 'white'
  bg = None
  
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
  def __init__(self, name, group, price):
    self.name = name
    self.price = price
    self.group = group
    self.owner = None 
    self.rent = (price/10) - 4
    self.determinecolor()   

  def __repr__(self):
    return self.name

  def chargerent(self):
    """Charges rent depending on monopoly.
      If owner owns all properties of a given color, he/she is able to charge twice the rent.
    """ 
    if self.owner.ismonopoly(self.group):
      print "You owe twice the rent since %s owns a monopoly!" % (self.owner)
      return 2*self.rent 
    return self.rent    

  def purchased(self, person):
    """Allows a given Player to purchase a card."""
    self.owner = person

  def sold(self):
    """Allows a given Player to sell the card back to the Bank."""
    self.owner = None 
  
  def determinecolor(self):
    #Determines the colors needed for the property when printing to terminal. 
    if self.group == 'purples':
      self.text = 'blue'
      self.bg = 'on_red'
    elif self.group == 'lightblues':
      self.text = 'blue' 
      self.bg = 'on_white'
    elif self.group == 'magentas':
      self.text = 'magenta' 
    elif self.group == 'oranges':
      self.text = 'red'
      self.bg = 'on_yellow'
    elif self.group == 'reds':
      self.text = 'red'
    elif self.group == 'yellows':
      self.text = 'yellow'
    elif self.group == 'greens':
      self.text = 'green'
    elif self.group == 'blues':
      self.text = 'blue'
    else:
      self.text = 'white'

class RailroadProperty(Property):
  def chargerent(self):
    if self.owner:
      self.rent = len(self.owner.owned['railroads'])*25 
      return self.rent
    else:
      return self.rent
