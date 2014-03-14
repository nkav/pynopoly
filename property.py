class Property:
  name = ""
  price = 0 
  owner = None 
  rent = 0 
  group = ''
  text = 'white'
  bg = None

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
      self.rent = len(self.owner.properties['railroads'])*25 
      return self.rent
    else:
      return self.rent
