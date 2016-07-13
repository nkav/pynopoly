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

def card(cardinfo, ui):
  ui.print_message("Your card was %s" % (cardinfo))

def advance_to_go(player, ui):
  card("to advance to go and collect $200!", ui) 
  player.advance(0)

def advance_to_oil(player, ui):
  card("to advance to Illinois Avenue.", ui)
  player.advance(24)

def advance_to_sc(player, ui):
  card("to advance to St. Charles Place.", ui)
  player.advance(11)

def advance_to_util(player, ui):
  card("to advance to the nearest Utility. If unowned, you can buy it. Otherwise, you must throw dice and pay the owner 10x the amount thrown.", ui)
  if player.position > 30 or player.position < 10:
    player.advance(12)
  else:
    player.advance(28)

def advance_to_rr(player, ui):
  card("to advance to the nearest Railroad. If unowned, you can buy it. Otherwise, you must pay the owner twice the normal rent.", ui)
  if player.position > 35 or player.position < 5:
    player.advance(5)
  elif player.position > 5 and player.position < 15:
    player.advance(15) 
  elif player.position > 15 and player.position < 25:
    player.advance(25) 
  else:
    player.advance(35)

def bank_pays_50(player, ui):
  card("the Bank pays you a dividend of $50. Congratulations!", ui)
  player.money += 50

def go_back_3(player, ui):
  card("go back 3 spaces!", ui)
  player.advance(player.position - 3)

def go_to_jail(player, ui):
  card("to go directly to jail!", ui)
  player.send_to_jail()
 
def poor_tax(player, ui):
  card("to pay a poor tax of $15.", ui)
  player.pay(15, None)

def reading_rr(player, ui):
  card("to advance to Reading Railroad. If unowned, you may buy it!", ui)
  player.advance(5)

def boardwalk(player, ui):
  card("to take a walk on Boardwalk! Advance directly to this space.", ui)
  player.advance(39)

def loan_matures(player, ui):
  card("to collect the returns on your mature building loan. Collect $150!", ui)
  player.money += 150
 
def crossword(player, ui):
  card("that you have won a crossword competition! Collect $100.", ui)
  player.money += 100

chance = [
  advance_to_go,
  advance_to_oil,
  advance_to_sc,
  advance_to_util,
  advance_to_rr,
  bank_pays_50,
  go_back_3,
  go_to_jail,
  poor_tax,
  reading_rr,
  boardwalk,
  loan_matures,
  crossword,
]

def bank_error(player, ui):
  card("to collect $75 from a bank error in your favor!", ui)
  player.money += 75 

def doctors_fees(player, ui):
  card("to pay $50 for doctor's fees. Ouch!", ui)
  player.money -= 50

def income_tax_refund(player, ui):
  card("to receive an income tax refund! Collect $20.", ui)
  player.money += 20

def life_insurance(player, ui):
  card("to collect $100 from mature life insurance.", ui)
  player.money += 100 

def hospital_fees(player, ui):
  card("to pay $100 for hospital fees.", ui)
  player.money -= 100

def school_fees(player, ui):
  card("to pay $50 for school fees.", ui)
  player.money -= 50

def consultancy_fee(player, ui):
  card("to receive $25 in consultancy fees.", ui)
  player.money += 25 

def beauty_contest(player, ui):
  card("to receive $10 for getting 2nd in a beauty contest.", ui)
  player.money += 10 

def inherit(player, ui):
  card("to inherit $100. Lucky day!", ui)
  player.money += 100

def sell_stocks(player, ui):
  card("to collect $50 from selling stock. Making bank!", ui)
  player.money += 50 

def holiday_fund(player, ui):
  card("to collect $100 from a mature holiday fund. Happy holidays!", ui)
  player.money += 100 

community_chest = [
  advance_to_go,
  bank_error,
  doctors_fees,
  go_to_jail,
  income_tax_refund,
  life_insurance,
  hospital_fees,
  school_fees,
  consultancy_fee,
  beauty_contest,
  inherit,
  sell_stocks,
  holiday_fund,  
]
