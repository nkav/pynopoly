chance = [
  advancetogo,
  advancetoil,
  advancetosc,
  advancetoutil,
  advancetorr,
  bankpays50,
  getoutofjail,
  goback3,
  gotojail,
  repairs,
  poortax,
  readingrr,
  boardwalk,
  youpay50,
  loanmatures,
  crossword
]

def chancecard(cardinfo):
  print "Your chance card was %s"

def advancetogo(player):
  chancecard("to advance to go and collect $200!") 
  player.position = 0
  player.passgo()
  player.checkbalance()

def advancetoil(player):
  chancecard("to advance to Illinois Avenue.")
  player.position = 24
  il = board[24]
  player.rentorbuy(il)

def advancetosc(player):
  chancecard("to advance to St. Charles Place.")
  player.position = 11
  sc = board[11]
  player.rentorbuy(sc)

def advancetoutil(player):
  chancecard("to advance to the nearest Utility. If unowned, you can buy it. Otherwise, you must throw dice and pay the owner 10x the amount thrown.")
  if player.position > 30 or player.position < 10:
    player.advance(12)
    util = board[12]
  else:
    player.advance(28)
    util = board[28]
  player.rentorbuy(util)

def advancetorr(player):
  chancecard("to advance to the nearest Railroad. If unowned, you can buy it. Otherwise, you must pay the owner twice the normal rent.") 
  if player.position > 35 or player.position < 5:
    player.advance(5)
    rr = board[5]
  elif player.position > 5 and player.position < 15:
    player.advance(15) 
    rr = board[15]
  elif player.position > 15 and player.position < 25:
    player.advance(25) 
    rr = board[25]
  else:
    player.advance(35)
    rr = board[35] 
  player.rentorbuy(rr)
