#!/usr/bin/env python
""" 
board.py - outlines the structure of the board 
"""

from Models.property import Property, RailroadProperty
from Models.community_chest import CommunityChest
from Models.chance import Chance
from Models.tax_space import TaxSpace
from Models.message_space import MessageSpace
from Models.jail import GoToJail

#spaces where user must draw a card
community_chests = [2, 17, 33]
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

prop_data = {
  'mediterranean': {
    'name': "Mediterranean Avenue",
    'group': 'purples',
    'price': 60,
    'rent': {
      0: 2,
      1: 10,
      2: 30,
      3: 90,
      4: 160,
      5: 250
    }
  },
  'baltic': {
    'name': "Baltic Avenue",
    'group': 'purples',
    'price': 60,
    'rent': {
      0: 4,
      1: 20,
      2: 60,
      3: 180,
      4: 320,
      5: 450
    }
  },
  'oriental': {
    'name': "Oriental Avenue",
    'group': 'lightblues',
    'price': 100,
    'rent': {
      0: 6,
      1: 30,
      2: 90,
      3: 270,
      4: 400,
      5: 550
    }
  },
  'vermont': {
    'name': "Vermont Avenue",
    'group': 'lightblues',
    'price': 100,
    'rent': {
      0: 6,
      1: 30,
      2: 90,
      3: 270,
      4: 400,
      5: 550
    }
  },
  'connecticut' : {
    'name': 'Connecticut Avenue', 
    'group': 'lightblues', 
    'price': 120,
    'rent': {
      0: 8, 
      1: 40,  
      2: 100,
      3: 300, 
      4: 450,
      5: 600
    },
  },
  'st_charles' : {
    'name': 'St. Charles Place', 
    'group': 'magentas', 
    'price': 140,
    'rent': {
      0: 10,  
      1: 50,  
      2: 150,
      3: 450, 
      4: 625,
      5: 750
    },
  },
  'electric' : {
    'name': 'Electric Company', 
    'group': 'utilities', 
    'price': 150,
    'rent': {
      0: 11,
    }
  },
  'states' : {
    'name': 'States Avenue', 
    'group': 'magentas', 
    'price': 140,
    'rent': {
      0: 10,  
      1: 50,  
      2: 150,
      3: 450, 
      4: 625,
      5: 750
    },
  },
  'virginia' : {
    'name': 'Virginia Avenue', 
    'group': 'magentas', 
    'price': 160,
    'rent': {
      0: 12,  
      1: 60,  
      2: 180,
      3: 500, 
      4: 700,
      5: 900
    },
  },
  'st_james' : {
    'name': 'St. James Place', 
    'group': 'oranges', 
    'price': 180,
    'rent': {
      0: 14,  
      1: 70,  
      2: 200,
      3: 550, 
      4: 750,
      5: 950
    },
  },
  'tennessee' : {
    'name': 'Tennessee Avenue', 
    'group': 'oranges', 
    'price': 180,
    'rent': {
      0: 14,  
      1: 70,  
      2: 200,
      3: 550, 
      4: 750,
      5: 950
    },
  },
  'new_york' : {
    'name': 'New York Avenue', 
    'group': 'oranges', 
    'price': 200,
    'rent': {
      0: 16,  
      1: 80,  
      2: 220,
      3: 600, 
      4: 800,
      5: 1000
    },
  },
  'kentucky' : {
    'name': 'Kentucky Avenue', 
    'group': 'reds', 
    'price': 220,
    'rent': {
      0: 18,  
      1: 90,  
      2: 250,
      3: 700, 
      4: 875,
      5: 1050
    },
  },
  'indiana' : {
    'name': 'Indiana Avenue', 
    'group': 'reds', 
    'price': 220,
    'rent': {
      0: 18,  
      1: 90,  
      2: 250,
      3: 700, 
      4: 875,
      5: 1050
    },
  },
  'illinois' : {
    'name': 'Illinois Avenue', 
    'group': 'reds', 
    'price': 240,
    'rent': {
      0: 20,  
      1: 100, 
      2: 300,
      3: 750, 
      4: 925,
      5: 1100
    },
  },
  'atlantic' : {
    'name': 'Atlantic Avenue', 
    'group': 'yellows', 
    'price': 260,
    'rent': {
      0: 22,  
      1: 110, 
      2: 330,
      3: 800, 
      4: 975,
      5: 1150
    },
  },
  'ventnor' : {
    'name': 'Ventnor Avenue', 
    'group': 'yellows', 
    'price': 260,
    'rent': {
      0: 22,  
      1: 110, 
      2: 330,
      3: 800, 
      4: 975,
      5: 1150
    },
    
  },
  'water' : {
    'name': 'Water Works', 
    'group': 'utilities', 
    'price': 150,
    'rent': {
      0: 11 #placeholder
    }
  },
  'marvin' : {
    'name': 'Marvin Gardens',
    'group': 'yellows', 
    'price': 280,
    'rent': {
      0: 24,  
      1: 120, 
      2: 360,
      3: 850, 
      4: 1025,
      5:  1200
    },
  },
  'pacific' : {
    'name': 'Pacific Avenue', 
    'group': 'greens', 
    'price': 300,
    'rent': {
      0: 26,  
      1: 130, 
      2: 390,
      3: 900, 
      4: 1100,
      5:  1275
    },
  },
  'north_carolina' : {
    'name': 'North Carolina Avenue', 
    'group': 'greens', 
    'price': 300,
    'rent': {
      0: 26,  
      1: 130, 
      2: 390,
      3: 900, 
      4: 1100,
      5:  1275
    },
  },
  'pennsylvania' : {
    'name': 'Pennsylvania Avenue', 
    'group': 'greens', 
    'price': 320,
    'rent': {
      0: 28,  
      1: 150, 
      2: 450,
      3: 1000,  
      4: 1200,
      5:  1400
    },
    
  },
  'park' : {
    'name': 'Park Place', 
    'group': 'blues', 
    'price': 350,
    'rent': {
      0: 35,  
      1: 175, 
      2: 500,
      3: 1100,  
      4: 1300,
      5:  1500
    },
  },
  'boardwalk' : {
    'name': 'Boardwalk', 
    'group': 'blues',
    'price':  40,
    'rent': {
      0: 50,  
      1: 200, 
      2: 600,
      3: 1400,  
      4: 1700,
      5:  2000
    },
  }
}

#dictionary binding of board indices [0,39] to Property types
#card spaces, tax spaces, jail, etc. are handled by Player.land()
chance_spot = Chance()
community_chest_spot = CommunityChest()

board = {
  0:  MessageSpace("Go", "Congrats!"),
  1:  Property(prop_data['mediterranean']),
  2:  chance_spot,
  3:  Property(prop_data['baltic']),
  4:  TaxSpace("Income Tax", 200),
  5:  RailroadProperty('Reading Railroad'),
  6:  Property(prop_data['oriental']),
  7:  community_chest_spot,
  8:  Property(prop_data['vermont']),
  9:  Property(prop_data['connecticut']),
  10: MessageSpace("Jail", "But you're just visiting!"),
  11: Property(prop_data['st_charles']),
  12: Property(prop_data['electric']),
  13: Property(prop_data['states']),
  14: Property(prop_data['virginia']),
  15: RailroadProperty('Pennsylvania Railroad'),
  16: Property(prop_data['st_james']),
  17: chance_spot,
  18: Property(prop_data['tennessee']),
  19: Property(prop_data['new_york']),
  20: MessageSpace("Free Parking", "Woo!"),
  21: Property(prop_data['kentucky']),
  22: community_chest_spot,
  23: Property(prop_data['indiana']),
  24: Property(prop_data['illinois']),
  25: RailroadProperty('B&O Railroad'),
  26: Property(prop_data['atlantic']),
  27: Property(prop_data['ventnor']),
  28: Property(prop_data['water']),
  29: Property(prop_data['marvin']),
  30: GoToJail(),
  31: Property(prop_data['pacific']),
  32: Property(prop_data['north_carolina']),
  33: chance_spot,
  34: Property(prop_data['pennsylvania']),
  35: RailroadProperty('Short Line'),
  36: community_chest_spot,
  37: Property(prop_data['park']),
  38: TaxSpace("Luxury Tax", 75),
  39: Property(prop_data['boardwalk'])
}
