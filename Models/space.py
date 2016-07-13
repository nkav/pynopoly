class Space(object):
	
	def __init__(self):
		self.owner = False
		self.group = "default"

	def label(self):
		return self.symbol

	def handle_land(self, player, roll, ui, simulate=False):
		pass