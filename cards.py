#!/usr/bin/env python
""" 
cards.py - Chance and Community Chest functionality for monpoly.

To be implemented:
  getoutofjail,
  birthday, # collect 50 from each player
  opera, # 50 from each player for opening night
  streetrepairs,
  getoutofjail,
  repairs,
  youpay50,
"""
from random import shuffle
from board import board

chanceindex = 0
communityindex = 0

def card(cardinfo):
  print "Your card was %s" % (cardinfo)

def advancetogo(player):
  card("to advance to go and collect $200!") 
  player.advance(0)

def advancetoil(player):
  card("to advance to Illinois Avenue.")
  player.advance(24)

def advancetosc(player):
  card("to advance to St. Charles Place.")
  player.advance(11)

def advancetoutil(player):
  card("to advance to the nearest Utility. If unowned, you can buy it. Otherwise, you must throw dice and pay the owner 10x the amount thrown.")
  if player.position > 30 or player.position < 10:
    player.advance(12)
  else:
    player.advance(28)

def advancetorr(player):
  card("to advance to the nearest Railroad. If unowned, you can buy it. Otherwise, you must pay the owner twice the normal rent.") 
  if player.position > 35 or player.position < 5:
    player.advance(5)
  elif player.position > 5 and player.position < 15:
    player.advance(15) 
  elif player.position > 15 and player.position < 25:
    player.advance(25) 
  else:
    player.advance(35)

def bankpays50(player):
  card("the Bank pays you a dividend of $50. Congratulations!")
  player.money += 50

def goback3(player):
  card("go back 3 spaces!")
  player.advance(player.position - 3)

def gotojail(player):
  card("to go directly to jail!")
  player.jailed()
 
def poortax(player):
  card("to pay a poor tax of $15.")
  player.pay(15, None)

def readingrr(player):
  card("to advance to Reading Railroad. If unowned, you may buy it!")
  player.advance(5)

def boardwalk(player):
  card("to take a walk on Boardwalk! Advance directly to this space.")
  player.advance(39)

def loanmatures(player):
  card("to collect the returns on your mature building loan. Collect $150!")
  player.money += 150
 
def crossword(player):
  card("that you have won a crossword competition! Collect $100.")
  player.money += 100

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
  crossword,
]

def bankerror(player):
  card("to collect $75 from a bank error in your favor!")
  player.money += 75 

def doctorsfees(player):
  card("to pay $50 for doctor's fees. Ouch!")
  player.money -= 50

def incometaxrefund(player):
  card("to receive an income tax refund! Collect $20.")
  player.money += 20

def lifeinsurance(player):
  card("to collect $100 from mature life insurance.")
  player.money += 100 

def hospitalfees(player):
  card("to pay $100 for hospital fees.")
  player.money -= 100

def schoolfees(player):
  card("to pay $50 for school fees.")
  player.money -= 50

def consultancyfee(player):
  card("to receive $25 in consultancy fees.")
  player.money += 25 

def beautycontest(player):
  card("to receive $10 for getting 2nd in a beauty contest.")
  player.money += 10 

def inherit(player):
  card("to inherit $100. Lucky day!")
  player.money += 100

def sellstocks(player):
  card("to collect $50 from selling stock. Making bank!")
  player.money += 50 

def holidayfund(player):
  card("to collect $100 from a mature holiday fund. Happy holidays!")
  player.money += 100 

communitychest = [
  advancetogo,
  bankerror,
  doctorsfees,
  gotojail,
  incometaxrefund,
  lifeinsurance,
  hospitalfees,
  schoolfees,
  consultancyfee,
  beautycontest,
  inherit,
  sellstocks,
  holidayfund,  
]

shuffle(chance)
shuffle(communitychest)
