from tkinter import *

class valueLine():

    def __init__(self, can):
        self.can = can    # stores the canvas
        self.value = 0     # value, shown by the line (often a random number)
        self.x_pos = 0    # the current position in an array of lines (doubles the index)
        self.x_step = 0   # the grafical step range from the x_limit, to multiply with x_pos
        self.x_limit = 0  # where the appearance of the lines begin on the canvas
        self.y_limit = 0  # the lower limit on the canvas
        self.line = None   # stores the grafical representation of the line (a 'widget')

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setx_pos(self, x):
        self.x_pos = x

    def getx_pos(self):
        return self.x_pos

    def setx_step(self, x):
        self.x_step = x

    def getx_step(self):
        return self.x_step

    def setx_limit(self, x):
        self.x_limit = x

    def sety_limit(self, y):
        self.y_limit = y

    def createLine(self):
        self.line = self.can.create_line(self.x_limit + self.x_pos*self.x_step, self.y_limit,
                                         self.x_limit + self.x_pos*self.x_step, self.y_limit - self.value,
                                         fill = 'white', width = 3, capstyle = ROUND)

    def highlight(self, color):
        self.line['fill'] = color

    def downlight(self):
        self.line['fill'] = 'white'

    def move(self, pos):
        self.x_pos = pos
        self.can.coords(self.line, self.x_limit + self.x_pos*self.x_step, self.y_limit,
                                         self.x_limit + self.x_pos*self.x_step, self.y_limit - self.value)
    

class linelist():

    def __init__(self):
        self.line = []
        self.maxValue=100
        self.minValue=0
        self.maxLine=20

        
