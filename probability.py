#!/usr/bin/env python
""" 
probability.py - probability for dice rolling, chancecards, and communitychestcards 
"""
import random

def die():
  """Rolls a 6-sided die"""
  return random.randint(1,6)

def chancecard():
  return random.randint(0,11)

def communitychestcard():
  return random.randint(0,12)
