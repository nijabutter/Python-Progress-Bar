class ProgressBar:
	def __init__(self,maximum, value=0, width=100, empty="░", full="█"):
		self.width = width
		self.empty = empty
		self.full = full
		self.value = value
		self.maximum = maximum
	def Show(self):
		self.Display(self.value)
	def Display(self,value):
		self.value = value
		print("\b" * (self.width+20), end='', flush=True)
		percent = float(self.value) / float(self.maximum)
		fill = int(percent * self.width)
		if fill > self.width: fill = self.width
		print(self.full * fill, end='', flush=True)
		print(self.empty * (self.width - fill), end='', flush=True)
		print(" " + str(int(percent * 100)) + "%", end='', flush=True)
	def SetMaximum(self,maximum):
		self.maximum = maximum
	def Add(self,value):
		self.value += value
	def Set(self,value):
		self.value = value
