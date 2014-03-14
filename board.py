#!/usr/bin/env python
""" 
board.py - outlines the structure of the board 
"""

from property import Property, RailroadProperty

#spaces where user must draw a card
communitychests = [2, 17, 33]
chances = [7, 22, 36] 

#groups that can be made into a monopoly
monopolizable = [
  'purples',
  'lightblues',
  'magentas',
  'oranges',
  'reds', 
  'yellows',
  'greens',
  'blues',
]

#dictionary binding of board indices [0,39] to Property types
#card spaces, tax spaces, jail, etc. are handled by the Player's self.land() function
board = {
  1:  Property('Mediterranean Avenue', 'purples', 60),
  3:  Property('Baltic Avenue', 'purples', 60),
  5:  RailroadProperty('Reading Railroad', 'railroads', 200),
  6:  Property('Oriental Avenue', 'lightblues', 100),
  8:  Property('Vermont Avenue', 'lightblues', 100),
  9:  Property('Connecticut Avenue', 'lightblues', 120),
  11: Property('St. Charles Place', 'magentas', 140),
  12: Property('Electric Company', 'utilities', 150),
  13: Property('States Avenue', 'magentas', 140),
  14: Property('Virginia Avenue', 'magentas', 160),
  15: RailroadProperty('Pennsylvania Railroad', 'railroads', 200),
  16: Property('St. James Place', 'oranges', 180),
  18: Property('Tennessee Avenue', 'oranges', 180),
  19: Property('New York Avenue', 'oranges', 200),
  21: Property('Kentucky Avenue', 'reds', 220),
  23: Property('Indiana Avenue', 'reds', 220),
  24: Property('Illinois Avenue', 'reds', 240),
  25: RailroadProperty('B&O Railroad', 'railroads', 200),
  26: Property('Atlantic Avenue', 'yellows', 260),
  27: Property('Ventnor Avenue', 'yellows', 260),
  28: Property('Water Works', 'utilities', 150),
  29: Property('Marvin Gardens', 'yellows', 280),
  31: Property('Pacific Avenue', 'greens', 300),
  32: Property('North Carolina Avenue', 'greens', 300),
  34: Property('Pennsylvania Avenue', 'greens', 320),
  35: RailroadProperty('Short Line', 'railroads', 200),
  37: Property('Park Place', 'blues', 350),
  39: Property('Boardwalk', 'blues', 400)
}
