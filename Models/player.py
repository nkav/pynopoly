#!/usr/bin/env python
""" 
player.py - creates functions for a Player 
"""

# TODO: include house/hotel value in properties

from probability import die
import math
from board import board, chances, community_chests, monopolizable
from Models.property import Property

class Player:
  """Monopoly player"""
  
  
  def __init__(self, name, order, ui, simulate=False):
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
    self.ui = ui
    self.order = order
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
    self.ui.print_message("%s is now in jail. You have %d more turns in jail." % (self, self.jailtime))

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
      self.ui.print_message("%s has a monopoly on %s!" % (self, group))
      return True
    else:
      return False

  def develop_monopolies(self):
    """Calls self.is_monopoly() for all group types owned."""

    for color in self.owned_by_group.keys():
      if self.is_monopoly(color):
        if not self.simulate:
          response = self.ui.raw_input("Would you like to buy or sell house(s) for the %s? (B)uy/(S)ell/(N)o [No]" % color) 
          if response in ("B", "Buy", ""):
            while True:
              num_houses = self.ui.raw_input("How many houses would you like to buy for the %s?" % color)
              if num_houses.isdigit():
                self.buy_houses(color, int(num_houses))
                break
              else:
                self.ui.print_message("That was not a number. Let's try that again.")
          elif response in ("S", "Sell"):
            while True:
              num_houses = self.ui.raw_input("How many houses would you like to sell for the %s?" % color)
              if num_houses.isdigit():
                self.sell_houses(color, int(num_houses))
                break
              else:
                self.ui.print_message("That was not a number. Let's try that again.")
        else:
          # TODO: override this function with AI class
          color_props = self.owned_by_group[color] # [prop1, prop2, prop3] all in one color group
          total_houses = sum(prop.houses for prop in color_props)
          max_houses = 5 * len(color_props)
          houses_to_buy = max_houses - total_houses
          if houses_to_buy:
            self.buy_houses(color, houses_to_buy)
          
 
  def buy_houses(self, color, num_houses):
    sorted_props = sorted(self.owned_by_group[color], key=lambda prop: prop.houses) #builds evenly from least developed
    num_of_props = Property.available[color]
    prop_index = 0
    houses_added = 0
    while num_houses:
      place = sorted_props[prop_index]
      if 1 + place.houses <= 5:
        if self.can_pay(place.house_price()):
          self.pay(place.house_price(), None)
          place.add_house()
          houses_added += 1
          num_houses -= 1
          prop_index += 1
          prop_index %= num_of_props
        else:
          self.ui.print_message("You don't have enough money!")
          break
      else:
        self.ui.print_message("Your properties are already fully developed on %s!" % (color))
        break
    self.ui.print_message("You just bought %d house(s) on the %s!" % (houses_added, color))
    self.check_balance()

  def sell_houses(self, color, num_houses):
    sorted_props = sorted(self.owned_by_group[color], key=lambda prop: prop.houses, reverse=True) #removes evenly from most developed
    prop_index = 0
    num_of_props = Property.available[color]
    houses_sold = 0
    while num_houses:
      place = sorted_props[prop_index]
      if place.houses - 1 >= 0:
        self.earn(place.house_price() * 0.5)
        place.remove_house()
        houses_sold += 1
        num_houses -= 1
        prop_index += 1
        prop_index %= num_of_props
      else:
        self.ui.print_message("You don't have any more houses to sell!")
        break
    self.ui.print_message("You've successfully sold %d house(s() on %s." (houses_sold, color))


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
        self.ui.print_message("You got doubles! You get to roll again at the end.")
        self.ui.print_message("Reminder: If you roll doubles %d more time(s) then you go to jail." % (2 - self.doublesrecord))
        self.doublesrecord += 1
        return False
    else:
      self.doublesrecord = 0
      return False
 
  def roll(self):
    """Rolls dice and then calls self.advance() to go to that function.
      If doubles is rolled a third time, Player goes directly to jail and does not advance.
    """
    self.ui.print_message("%s's turn." % (self))
    self.check_balance()
    self.develop_monopolies()
    if not self.simulate:
      self.ui.raw_input("Enter to roll. ")
    die1 = die()
    die2 = die()
    dice = die1 + die2 
    self.ui.print_message("%s rolled a %d and %d to get %d." % (self, die1, die2, dice))
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
    current_spot.handle_land(self, roll, self.ui)   
    if doubles:
      self.ui.print_message("Roll again!")
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
      self.ui.print_message("Lucky you, you landed on Go! You collect $400!" )
      self.earn(400)
    elif location > 40:
      self.position = location % 40
      self.ui.print_message("%s just passed Go and collected $200!"  % self)
      self.earn(200)
    elif location < 0:
      self.position = 40 + location
    else:
      self.position = location
      
    self.ui.refresh_players() 
    self.land(doubles, roll=roll)
        
  def check_balance(self):
    self.ui.print_message("%s's current balance is $%d." % (self, self.money))
    
  
  def earn(self, money):
    self.money += money
    self.check_balance()


  def can_pay(self, amount):
    return self.money >= amount

  def pay(self, amount, owner):
    if self.money >= amount:
      self.money -= amount
      self.check_balance()
      if owner:
        owner.earn(amount)
        self.ui.print_message("%s just paid $%d to %s." % (self, amount, owner))
      # if no owner money is paid to the bank
    else:
      self.ui.print_message("%s doesn't have enough money to pay %s! %s is out of the game." % (self, owner, self))
      self.bankrupt = True
 
  def add_property(self, place):
    self.owned_by_group[place.group].append(place)
    place.purchase(self)
    self.ui.print_board()
    self.ui.print_message("%s just purchased %s for $%d." % (self, place.name, place.price))

  def mortgage_property(self, place):
    if not property.is_mortgaged():
      property.mortgage()
      self.ui.print_message("You have now mortgaged %s for $%d!" (place, place.mortgage_value()))
      player.earn(property.mortgage_value())
    else:
      self.ui.print_message("%s is already mortgaged!" % place)


  def unmortgage_property(self, place):
    if property.is_mortgaged():
      if self.can_pay(property.price_to_unmortgage):
        self.pay(property.price_to_unmortgage, None)
        property.unmortgage()
        self.ui.print_message("You have now unmortgaged %s for $%d!" (place, property.price_to_unmortgage))
    else:
      self.ui.print_message("%s is already mortgaged!" % place)

  def buy(self, place):
    """If the user does not already own the property, no one else owns property, 
      and user has enough money, then user can buy property.
    """
    response = ''
    if not self.simulate: 
      while response not in ('Y', 'N'):
        response = self.ui.raw_input("Will you buy %s for $%d? (Y/N) " % (place.name, place.price))
    else:
      response = 'Y'
    if (response == 'Y'):
      if self.can_pay(place.price):
        self.add_property(place)
        self.pay(place.price, None)
      else:
        self.ui.print_message("%s doesn't have enough money to purchase the property!" % (self))
