from sortlist import linelist
from time import sleep

class bubble():
    def __init__(self):
        self.linelist = None
        self.count = 0
        self.maxCount = 0
        self.swapped = False

    def setList(self, l1):
        self.linelist = l1

    def initSort(self):
        self.maxCount = self.linelist.getMaxLine()
        self.count = 0

    def step(self):
        if self.linelist.getLineValue(self.count) > self.linelist.getLineValue(self.count + 1):
            self.linelist.swapEls(self.count, self.count + 1)
            self.swapped = True
        else:
            self.linelist.setDownlight(self.count)
            self.linelist.setHighlight(self.count+1)
        self.count += 1
        if self.count >= self.maxCount -1:
            self.linelist.setDownlight(self.count)
            self.maxCount -=1
            self.count = 0
        if self.maxCount <= 1:
            return False
        return True
