class ProgressBar:
    def __init__(self, value=0, maximum=100, length=25, empty='░', fill='█'):
        self.value = value
        self.maximum = maximum
        self.length = length
        self.empty = empty
        self.fill = fill
    def get(self):
        percent = float(self.value) / float(self.maximum)
        fill = int(percent * self.length)
        empty = self.length - fill
        return (self.fill * fill) + (self.empty * empty) + " " + str(int(percent*100)).rjust(3) + "%"
    def set(self, value):
        self.value = value
        if self.value > self.maximum:
            self.value = self.maximum
