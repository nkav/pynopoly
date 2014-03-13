from probability import die
from graphics import printplayer, printboard
import math
from board import board, chances, communitychests

class Player:
  """Monopoly player"""
  name = ""
  position = 0 #Start at Go
  money = 2000
  bankrupt = False
  jailtime = 0
  properties = {
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
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

  def servetime(self):
    if (self.jailtime > 0):
      self.jailtime -= 1
      return True 
    return False 
  
  def rentorbuy(self, place):
    targetproperty = board[place]
    propertyowner = targetproperty.owner
    if (targetproperty in sum(self.properties.values(), [])):
      print "%s already owns %s!" % (self.name, targetproperty)
    elif propertyowner: 
      print "This property is already owned by by %s. %s must pay rent." % (propertyowner, self.name)
      self.payrent(targetproperty)
    else:
      self.buy(targetproperty)

  def roll(self):
    dice = die() + die()
    print "%s rolled %d." % (self.name, dice)
    self.advance(self.position + dice)
    printboard()
    printplayer('X', self.position)
    if self.position in board.keys():
      currentspot = board[self.position]
      print "Landed on %s." % (currentspot)
      self.rentorbuy(self.position)
    elif self.position in chances:
      print "Chance!"
    elif self.position in communitychests:
      print "Community Chest!"
    elif self.position == 30:
      self.jailtime = 2
      self.position = 10
      print "%s are now in jail. You have %d more turns in jail." % (self.name, self.jailtime)
    elif self.position == 0:
      print "%s just landed on Go! Congrats!" % (self.name)            
    elif self.position == 20:
      print "Landed on Free Parking! Woo!"
    elif self.position == 10:
      print "Landed on Jail - but just visiting!"
    elif self.position == 38:
      print "Landed on Luxury Tax. You'll need to pay $75!"
      self.pay(75)
    elif self.position == 4:
      print "You landed on Income Tax. You will be charged $200 or 10% of your total assets."
      self.pay(min(200, self.totalassets))
    self.checkbalance()  
      
  def totalassets(self):
    assets = self.money
    for place in sum(self.properties.values(), []):
      assets += place.price
    return assets

  def advance(self, location):
    location = location % 40 
    if location >= self.position:
      self.position = location
    else:
      self.position = location
      self.money += 200
      print "You just passed go and collected $200!"  
      self.checkbalance()
        
  def checkbalance(self):
    print "Your current balance is %d." % (self.money)

  def payrent(self, place):
    rent = place.chargerent()  
    self.pay(rent)
    print "%s just paid %d in rent for landing on %s." % (self.name, rent, place.name) 

  def pay(self, amount):
    if self.money >= amount:
      self.money -= amount
      return True 
    else:
      return False
 
  def addproperty(self, place):
    self.properties[place.group].append(place)
    place.purchased(self)

  def buy(self, place):
    if (place in sum(self.properties.values(), [])):
      return "%s already owns this property!" % (self.name)
    elif place.owner:
      return "The property is already owned by %s." % (place.owner)
    else:
      response = ''
      while ((response != 'Y') and (response != 'N')):
        response = raw_input("Will you buy %s for %d? (Y/N) " % (place.name, place.price))
      if (response == 'Y'):
        if (self.pay(place.price)):
          self.addproperty(place)
          print "%s just purchased %s for %d." % (self.name, place.name, place.price)
        else:
          print "%s doesn't have enough money to purchase the property!" % (self.name)
