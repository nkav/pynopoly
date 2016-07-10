#!/usr/bin/env python
""" 
player.py - creates functions for a Player 
"""

# TODO: include house/hotel value in properties

from probability import die
from graphics import print_player, print_board, new_screen, properties_owned, section_break
import math
from board import board, chances, community_chests, monopolizable
from property import Property
import copy
import cards

class Player:
  """Monopoly player"""
  bankrupt = False #If a player is ever unable to pay rent, then he/she loses game
  jailtime = 0 #If greater than 0, user is in jail for that number many more turns
  money = 2000 #Default starting money
  position = 0 #Start at Go
  doublesrecord = 0 #Number of doubles at any given moment. 3 doubles means go to jail
  simulate = False #Faster version that defaults to buying property and skipping inputs
  
  def __init__(self, name, simulate=False):
    """Initialize new Player
      args:
      name -- string of the player's name
      kwargs:
      simulate -- Defaults to false. If True, faster version of game is played where inputs are skipped
                  and properties are bought by default
    """
    
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
    self.simulate = simulate

  def __repr__(self):
    return self.name

  def servetime(self):
    """Serve time in jail
      If player needs to serve more terms in jail, the function decrements jailtime.
      It returns True if the Player needs to serve more time, or False if Player has finished serving
    """ 
    if (self.jailtime > 0):
      self.jailtime -= 1
      return True 
    return False 

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
          prop = sorted(color, key=lambda prop: prop.houses)[0]
          prop.add_house()
          self.pay(100, None)
          print "You just bought a house on %s!" % prop.name 
 
  def rent_or_buy(self, place):
    """Checks if a property is owned, and then either pays rent or buys."""
    targetproperty = board[place]
    propertyowner = targetproperty.owner
    if (targetproperty in sum(self.owned_by_group.values(), [])):
      print "%s already owns %s!" % (self, targetproperty)
    elif propertyowner: 
      print "This property is already owned by by %s. %s must pay rent." % (propertyowner, self)
      self.pay_rent(targetproperty)
    else:
      self.buy(targetproperty)

  def doubles_jail(self, die1, die2):
    """Takes dice rolled and checks if the user has rolled dice 3 times.
      args:
      die1, die2 -- dice that were rolled for this given turn
    """
    if die1 == die2:
      if self.doublesrecord == 2:
        "You got doubles a third time! You go straight to jail!"
        self.doublesrecord = 0
        self.jailed()
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
    self.advance(self.position + dice, doubles=doubles)

  def land(self, doubles):
    """Determines what to do when landing on a given space.
      args:
      doubles -- if True, self.roll() is called again at the end of this function
    """
    if self.position in board.keys():
      current_spot = board[self.position]
      print "Landed on %s." % (current_spot)
      self.rent_or_buy(self.position)
    elif self.position in chances:
      print "You landed on Chance!"
      if not self.simulate:
        raw_input("Enter to draw a card. ")
      cards.chance[cards.chance_index](self)
      cards.chance_index += 1
      cards.chance_index %= len(cards.chance)
    elif self.position in community_chests:
      print "You landed on Community Chest!"
      if not self.simulate:
        raw_input("Enter to draw a card. ")
      cards.communitychest[cards.community_index](self)
      cards.community_index += 1
      cards.community_index %= len(cards.communitychest)
    elif self.position == 30:
      print "You landed on Go to Jail!"
      self.jailed()
    elif self.position == 0:
      print "%s just landed on Go! Congrats!" % (self)            
    elif self.position == 4:
      print "You landed on Income Tax. You will be charged the lesser of $200 or 10% of your total assets."
      print "Your total assets: $" + str(self.total_assets())
      self.pay(min(200, 0.1*self.total_assets()), None)
    elif self.position == 10:
      print "Landed on Jail - but just visiting!"
    elif self.position == 20:
      print "Landed on Free Parking! Woo!"
    elif self.position == 38:
      print "Landed on Luxury Tax. You'll need to pay $75!"
      self.pay(75, None)
    self.check_balance()  
    section_break()
    if not self.simulate:
      raw_input("Enter to continue. ")
    new_screen()
    if doubles:
      print "Roll again!"
      self.roll()
     
  def jailed(self):
    """Function that places user in jail and sets their jailtime to 3 turns."""
    self.jailtime = 2
    self.position = 10 
    print "%s is now in jail. You have %d more turns in jail." % (self, self.jailtime)

  def total_assets(self):
    """Values the user's total assets for the income tax space."""
    assets = self.money
    for place in sum(self.owned_by_group.values(), []):
      assets += place.price
    return assets
  
  def advance(self, location, doubles=False):
    """Advances to the given location.
      If passing go, user receives $200
      args:
      location mod 40 -- numerical space on board where advancing to.
      kwargs:
      doubles -- If True, then passes argument to self.land() function.
    """
    if location == 40:
      self.position = 0
      self.money += 400
      print "Lucky you, you landed on Go! You collect $400!"  
      self.check_balance()
    elif location > 40:
      self.position = location % 40
      self.money += 200
      print "You just passed Go and collected $400!"  
      self.check_balance()
    else:
      self.position = location
      
    print_board()
    print_player(self.name, self.position) 
    self.land(doubles)
        
  def check_balance(self):
    print "%s's current balance is $%d." % (self, self.money)

  def pay_rent(self, place):
    rent = place.get_rent()  
    if(self.pay(rent, place.owner)):
      print "%s just paid $%d in rent to %s for landing on %s." % (self, rent, place.owner, place.name) 
    else:
      print "%s doesn't have enough money to pay rent! You are out of the game." % (self)
      self.bankrupt = True
      
  def pay(self, amount, owner):
    if self.money >= amount:
      self.money -= amount
      if owner:
        owner.money += amount
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
    if (place in sum(self.owned_by_group.values(), [])):
      return "%s already owns this property!" % (self)
    elif place.owner:
      return "The property is already owned by %s." % (place.owner)
    else:
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
