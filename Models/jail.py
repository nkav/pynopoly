from space import Space

class GoToJail(Space):
	def __init__(self):
		self.symbol = "j"
		self.group = 'default'

	def handle_land(self, player, roll, ui, simulate=False):
		ui.print_message("You landed on Go to Jail! You have the right to remain silent...")
		player.send_to_jail()