from board import board

def chancecard(cardinfo):
  print "Your chance card was %s" % (cardinfo)

def advancetogo(player):
  chancecard("to advance to go and collect $200!") 
  player.advance(0)

def advancetoil(player):
  chancecard("to advance to Illinois Avenue.")
  player.advance(24)

def advancetosc(player):
  chancecard("to advance to St. Charles Place.")
  player.advance(11)

def advancetoutil(player):
  chancecard("to advance to the nearest Utility. If unowned, you can buy it. Otherwise, you must throw dice and pay the owner 10x the amount thrown.")
  if player.position > 30 or player.position < 10:
    player.advance(12)
  else:
    player.advance(28)

def advancetorr(player):
  chancecard("to advance to the nearest Railroad. If unowned, you can buy it. Otherwise, you must pay the owner twice the normal rent.") 
  if player.position > 35 or player.position < 5:
    player.advance(5)
  elif player.position > 5 and player.position < 15:
    player.advance(15) 
  elif player.position > 15 and player.position < 25:
    player.advance(25) 
  else:
    player.advance(35)

def bankpays50(player):
  chancecard("the Bank pays you a dividend of $50. Congratulations!")
  player.money += 50

def goback3(player):
  chancecard("go back 3 spaces!")
  player.advance(player.position - 3)

def gotojail(player):
  chancecard("to go directly to jail!")
  player.jailed()
 
def poortax(player):
  chancecard("to pay a poor tax of $15.")
  player.pay(15, None)

def readingrr(player):
  chancecard("to advance to Reading Railroad. If unowned, you may buy it!")
  player.advance(5)

def boardwalk(player):
  chancecard("to take a walk on Boardwalk! Advance directly to this space.")
  player.advance(39)

def loanmatures(player):
  chancecard("to collect the returns on your mature building loan. Collect $150!")
  player.money += 150
 
chance = [
  advancetogo,
  advancetoil,
  advancetosc,
  advancetoutil,
  advancetorr,
  bankpays50,
  goback3,
  gotojail,
  readingrr,
  boardwalk,
  loanmatures,
]

"""To be implemented:
  getoutofjail,
  repairs,
  crossword
  youpay50,
"""

