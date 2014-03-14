class Property:
  name = ""
  price = 0 
  owner = None 
  rent = 0 
  group = ''
  text = 'white'
  bg = None

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
    if self.owner.ismonopoly(self.group, Property.available[self.group]):
      print "You owe twice the rent since %s owns a monopoly!" % (self.owner)
      raw_input("We have monopoly rent! ")
      return 2*self.rent 
    return self.rent    

  def purchased(self, person):
    self.owner = person

  def sold(self):
    self.owner = None 
  
  def determinecolor(self):
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
