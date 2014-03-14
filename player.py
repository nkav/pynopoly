from probability import die
from graphics import printplayer, printboard, newscreen
import math
from board import board, chances, communitychests
import copy

class Player:
  """Monopoly player"""
  bankrupt = False
  jailtime = 0
  money = 2000
  position = 0 #Start at Go
  doublesrecord = 0
  owned = {
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
    self.owned = copy.deepcopy(Player.owned)

  def __repr__(self):
    return self.name

  def servetime(self):
    if (self.jailtime > 0):
      self.jailtime -= 1
      return True 
    return False 

  def jailtimeleft(self):
    print "%s is now in jail. You have %d more turns in jail." % (self, self.jailtime)
    raw_input("Enter to continue. ")
    newscreen()
 
  def rentorbuy(self, place):
    targetproperty = board[place]
    propertyowner = targetproperty.owner
    if (targetproperty in sum(self.owned.values(), [])):
      print "%s already owns %s!" % (self, targetproperty)
    elif propertyowner: 
      print "This property is already owned by by %s. %s must pay rent." % (propertyowner, self)
      self.payrent(targetproperty)
    else:
      self.buy(targetproperty)

  def doublesjail(self, die1, die2):
    if die1 == die2:
      if self.doublesrecord == 2:
        "You got doubles a third time! You go straight to jail!"
        self.doublesrecord = 0
        self.jailed()
        return True
      else:
        print "You got doubles! You get to roll again at the end. If you roll doubles %d more time(s) then you go to jail." % (2 - self.doublesrecord)
        self.doublesrecord += 1
        return False
    else:
      self.doublesrecord = 0
      return False
 
  def roll(self):
    self.checkbalance()
    propertiesowned(self.owned)
    raw_input("Enter to roll. ")
    die1 = die()
    die2 = die()
    dice = die1 + die2 
    print "%s rolled a %d and %d to get %d." % (self, die1, die2, dice)
    if self.doublesjail(die1, die2):
      return None
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
      print "You landed on Go to Jail!"
      self.jailed()
    elif self.position == 0:
      print "%s just landed on Go! Congrats!" % (self)            
    elif self.position == 4:
      print "You landed on Income Tax. You will be charged the lesser of $200 or 10% of your total assets."
      self.pay(min(200, self.totalassets), None)
    elif self.position == 10:
      print "Landed on Jail - but just visiting!"
    elif self.position == 20:
      print "Landed on Free Parking! Woo!"
    elif self.position == 38:
      print "Landed on Luxury Tax. You'll need to pay $75!"
      self.pay(75, None)
    self.checkbalance()  
    raw_input("Enter to continue. ")
    newscreen()
    if (die1 == die2):
      print "Roll again!"
      self.roll()
     
  def jailed(self):
    self.jailtime = 2
    self.position = 10 
    print "%s is now in jail. You have %d more turns in jail." % (self, self.jailtime)

  def totalassets(self):
    assets = self.money
    for place in sum(self.owned.values(), []):
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
    print "Your current balance is $%d." % (self.money)

  def payrent(self, place):
    rent = place.chargerent()  
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
 
  def addproperty(self, place):
    self.owned[place.group].append(place)
    place.purchased(self)

  def buy(self, place):
    if (place in sum(self.owned.values(), [])):
      return "%s already owns this property!" % (self)
    elif place.owner:
      return "The property is already owned by %s." % (place.owner)
    else:
      response = ''
      while ((response != 'Y') and (response != 'N')):
        response = raw_input("Will you buy %s for $%d? (Y/N) " % (place.name, place.price))
      if (response == 'Y'):
        if (self.pay(place.price, None)):
          self.addproperty(place)
          print "%s just purchased %s for $%d." % (self, place.name, place.price)
        else:
          print "%s doesn't have enough money to purchase the property!" % (self)
