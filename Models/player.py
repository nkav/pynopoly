#!/usr/bin/env python
""" 
player.py - creates functions for a Player 
"""

# TODO: include house/hotel value in properties

from probability import die
from graphics import print_player, print_board, new_screen, properties_owned, section_break
import math
from board import board, chances, community_chests, monopolizable
from Models.property import Property

class Player:
  """Monopoly player"""
  
  
  def __init__(self, name, simulate=False):
    """Initialize new Player
      args:
      name -- string of the player's name
      kwargs:
      simulate -- Defaults to false. If True, faster version of game is played where inputs are skipped
                  and properties are bought by default
    """
    self.bankrupt = False #If a player is ever unable to pay rent, then he/she loses game
    self.jailtime = 0 #If greater than 0, user is in jail for that number many more turns
    self.money = 2000 #Default starting money
    self.position = 0 #Start at Go
    self.doublesrecord = 0 #Number of doubles at any given moment. 3 doubles means go to jail
    self.simulate = simulate #Faster version that defaults to buying property and skipping inputs
    self.name = name
    self.owned_by_group = {
      'railroads': [],
      'utilities': [],
      'purples': [],
      'lightblues': [],
      'magentas': [],
      'oranges': [],
      'reds': [],
      'yellows': [],
      'greens': [],
      'blues': []
    } 

  def __repr__(self):
    return self.name

  def in_jail(self):
    return True if self.jailtime > 0 else False

  def serve_time(self):
    """Serve time in jail
      If player needs to serve more terms in jail, the function decrements jailtime.
      It returns True if the Player needs to serve more time, or False if Player has finished serving
    """ 
    if self.jailtime > 0:
      self.jailtime -= 1
      self.jail_time_left()

  def jail_time_left(self):
    """Replacement for user turn
      If a player is in jail, then this function will be called.
      It notifies the user how many more turns in needs to serve in Jail.
    """
    print "%s is now in jail. You have %d more turns in jail." % (self, self.jailtime)
    if not self.simulate:
      raw_input("Enter to continue. ")
    new_screen()

  def is_monopoly(self, group):
    """Checks if the Player has a monopoly on the given group type.
      args:
      group -- the string of the group type
      Returns false if the group type is not monopolizeable.
      Returns true if Player owns all properties in that group type.
      Returns false if Player does not own all properties in that group type.
    """  
    if group not in monopolizable:
      return False
    elif len(self.owned_by_group[group]) == Property.available[group]:
      print "%s has a monopoly on %s!" % (self, group) 
      return True
    else:
      return False

  def hasmonopoly(self):
    """Calls self.is_monopoly() for all group types owned."""
    for key in self.owned_by_group.keys():
      if self.is_monopoly(key):
        if not self.simulate:
          response = raw_input("Would you like to buy a house for the %s? (Y/N)" %key) 
        else:
          response = 'Y'
        if response == "Y":
          color = self.owned_by_group[key] # [prop1, prop2, prop3] all in one color group
          # TODO: allow user to choose which property to develop
          prop = sorted(color, key=lambda prop: prop.houses)[0] # develops evenly
          prop.add_house()
          
 
  def rent_or_buy(self, place):
    """Checks if a property is owned, and then either pays rent or buys."""
    if place.owner == self:
      print "%s already owns %s!" % (self, place.name)
    elif place.owner: 
      print "This property is already owned by by %s. %s must pay rent." % (place.owner, self)
      self.pay_rent(place)
    else:
      self.buy(place)

  def doubles_jail(self, die1, die2):
    """Takes dice rolled and checks if the user has rolled dice 3 times.
      args:
      die1, die2 -- dice that were rolled for this given turn
    """
    if die1 == die2:
      if self.doublesrecord == 2:
        "You got doubles a third time! You go straight to jail!"
        self.doublesrecord = 0
        self.send_to_jail()
        return True
      else:
        print "You got doubles! You get to roll again at the end."
        print "Reminder: If you roll doubles %d more time(s) then you go to jail." % (2 - self.doublesrecord)
        self.doublesrecord += 1
        return False
    else:
      self.doublesrecord = 0
      return False
 
  def roll(self):
    """Rolls dice and then calls self.advance() to go to that function.
      If doubles is rolled a third time, Player goes directly to jail and does not advance.
    """
    self.check_balance()
    properties_owned(self)
    self.hasmonopoly()
    section_break()
    if not self.simulate:
      raw_input("Enter to roll. ")
    die1 = die()
    die2 = die()
    dice = die1 + die2 
    print "%s rolled a %d and %d to get %d." % (self, die1, die2, dice)
    if self.doubles_jail(die1, die2):
      return None
    doubles = die1 == die2
    self.advance(self.position + dice, roll=dice, doubles=doubles)

  def land(self, doubles, roll=None):
    """Determines what to do when landing on a given space.
      args:
      doubles -- if True, self.roll() is called again at the end of this function
    """
    current_spot = board[self.position]
    current_spot.handle_land(self, roll)   
    section_break()
    if not self.simulate:
      raw_input("Enter to continue. ")
    new_screen()
    if doubles:
      print "Roll again!"
      self.roll()
     

  def send_to_jail(self):
    """Function that places user in jail and sets their jailtime to 3 turns."""
    self.jailtime = 2
    self.position = 10 
    self.jail_time_left()

  def total_assets(self):
    """Values the user's total assets for the income tax space."""
    if self.bankrupt:
      return 0
    assets = self.money
    for place in sum(self.owned_by_group.values(), []):
      assets += place.price
    return assets
  
  def advance(self, location, roll=None, doubles=False):
    """Advances to the given location.
      If passing go, user receives $200
      args:
      location mod 40 -- numerical space on board where advancing to.
      kwargs:
      doubles -- If True, then passes argument to self.land() function.
    """
    if location == 40:
      self.position = 0
      print "Lucky you, you landed on Go! You collect $400!" 
      self.earn(400)
    elif location > 40:
      self.position = location % 40
      print "You just passed Go and collected $200!"  
      self.earn(200)
    elif location < 0:
      self.position = 40 + location
    else:
      self.position = location
      
    print_board()
    print_player(self.name, self.position) 
    self.land(doubles, roll=roll)
        
  def check_balance(self):
    print "%s's current balance is $%d." % (self, self.money)

  def pay_rent(self, place):
    if place.mortgaged:
      print "%s is mortgaged! %s does not have to pay %s anything." % (place, self, place.owner)
    else:
      rent = place.get_rent()
      print "Rent for %s is $%d" % (place, rent)
      if self.pay(rent, place.owner):
        print "%s just paid $%d in rent to %s for landing on %s." % (self, rent, place.owner, place.name) 
      else:
        print "%s doesn't have enough money to pay rent! You are out of the game." % (self)
        self.bankrupt = True
  
  def earn(self, money):
    self.money += 400
    self.check_balance()

  def pay(self, amount, owner):
    if self.money >= amount:
      self.money -= amount
      self.check_balance()
      if owner:
        owner.money += amount
      # if no owner money is paid to the bank
      return True 
    else:
      return False
 
  def add_property(self, place):
    self.owned_by_group[place.group].append(place)
    place.purchased(self)

  def buy(self, place):
    """If the user does not already own the property, no one else owns property, 
      and user has enough money, then user can buy property.
    """
    response = ''
    if not self.simulate: 
      while response not in ('Y', 'N'):
        response = raw_input("Will you buy %s for $%d? (Y/N) " % (place.name, place.price))
    else:
      response = 'Y'
    if (response == 'Y'):
      if (self.pay(place.price, None)):
        self.add_property(place)
        print "%s just purchased %s for $%d." % (self, place.name, place.price)
      else:
        print "%s doesn't have enough money to purchase the property!" % (self)
