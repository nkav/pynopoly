#!/usr/bin/env python
""" 
curses_ui.py - functions for the curses interface
"""

import curses, locale

class CursesUI:

  BOARD_Y = 8
  PLAYERS_Y = 9
  MESSAGE_Y = 16
  MESSAGE_X = 5
  MESSAGE_HEIGHT = 5

  color_pairs = {
    'purples': 4,
    'lightblues': 6,
    'magentas': 5,
    'oranges': 3,
    'reds': 1,
    'yellows': 3,
    'greens': 2,
    'blues': 4,
    'railroads': 7,
    'utilities': 7,
    'default': 7
  }
  
  def __init__(self, players, board, simulate=False):
    self.players = players
    self.simulate = simulate
    self.board = board
    self.set_encoding()
    self.start()
    self.init_colors()
    self.display_title()

  def refresh_players(self):
    self.player_display.erase()
    centered_x = (self.width - 80)/2
    for player in self.players:
      self.player_display.addstr(player.order, centered_x + player.position*2, "^ " + player.name)
    self.player_display.refresh()


  def set_encoding(self):
    locale.setlocale(locale.LC_ALL, '')
    self.code = locale.getpreferredencoding()

  def init_colors(self):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_WHITE)

  def start(self):
    self.screen = curses.initscr()
    self.screen.border(0) # put a border around the terminal
    curses.start_color() # initialize colors
    self.height,self.width = self.screen.getmaxyx()
    self.player_display = curses.newwin(6, self.width, CursesUI.PLAYERS_Y, 0)
    self.messages = curses.newwin(CursesUI.MESSAGE_HEIGHT, self.width - (CursesUI.MESSAGE_X*2), CursesUI.MESSAGE_Y, CursesUI.MESSAGE_X)
    

  def display_title(self):
    text = "MONOPOLY"
    centered_x = (self.width - len(text))/2
    self.screen.addstr(0, centered_x, text)
    self.screen.refresh()

  def print_message(self, message):
    self.messages.erase()
    self.messages.addstr(0, 0, message)
    self.messages.refresh()
    if not self.simulate:
      self.messages.getch()

  def raw_input(self, message):
    self.messages.clear()
    self.messages.addstr(0, 0, message)
    self.messages.refresh()
    c = 'Y'
    if not self.simulate:
      c = chr(self.messages.getch())
    return c



  def print_board(self):
    centered_x = (self.width - 80)/2
    for space in self.board:
      self.screen.addstr(CursesUI.BOARD_Y, centered_x + (space*2), (self.board[space].label()+" ").encode(self.code), curses.color_pair(CursesUI.color_pairs[self.board[space].group]))
    self.screen.refresh()

  def exit(self):
    curses.nocbreak(); self.screen.keypad(0); curses.echo()
    curses.endwin()