class Property:
  name = ""
  price = 0 
  owner = None 
  rent = 0 
  group = ''

  def __init__(self, name, group, price):
    self.name = name
    self.price = price
    self.group = group
    self.owner = None 
    self.rent = (price/10) - 4

  def __repr__(self):
    return self.name

  def chargerent(self):
    return self.rent    

  def purchased(self, person):
    self.owner = person

  def sold(self):
    self.owner = None 

class RailroadProperty(Property):
  def chargerent(self):
    if self.owner:
      self.rent = len(self.owner.properties['railroads'])*25 
      return self.rent
    else:
      return self.rent
