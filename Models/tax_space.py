from space import Space

class TaxSpace(Space):
	def __init__(self, name, amount):
		self.name = name
		self.amount = amount
		self.symbol = "$"
		self.group = 'default'

	def handle_land(self, player, roll, ui, simulate=False):
		ui.print_message("You landed on %s. You owe $%d." % (self.name, self.amount))
		player.pay(self.amount, None)
		player.check_balance()	