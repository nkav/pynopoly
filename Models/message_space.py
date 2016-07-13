from space import Space

class MessageSpace(Space):
	def __init__(self, name, message):
		self.name = name
		self.message = message
		self.symbol = name[0]
		self.group = 'default'


	def handle_land(self, player, roll, ui, simulate=False):
		ui.print_message("You landed on %s! %s" % (self.name, self.message))