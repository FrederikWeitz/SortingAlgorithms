from tkinter import *
import random

class valueLine():

    def __init__(self, can):
        self.can = can    # stores the canvas
        self.value = 0     # value, shown by the line (often a random number)
        self.x_pos = 0    # the current position in an array of lines (doubles the index)
        self.x_step = 0   # the grafical step range from the x_limit, to multiply with x_pos
        self.x_limit = 0  # where the appearance of the lines begin on the canvas
        self.y_limit = 0  # the lower limit on the canvas
        self.line = None   # stores the grafical representation of the line (a 'widget')

    def delete(self):
        self.can.delete(self.line)

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
        self.can.itemconfigure(self.line, fill=color)

    def downlight(self):
        self.can.itemconfigure(self.line, fill='white')

    def move(self, pos):
        if type(pos)==int:
            self.x_pos = pos
        elif type(pos)==list:
            self.x_pos = pos[0]
        else:
            return
        self.can.coords(self.line, self.x_limit + self.x_pos*self.x_step, self.y_limit,
                                         self.x_limit + self.x_pos*self.x_step, self.y_limit - self.value)
        self.can.update_idletasks()
    

class linelist():

    def __init__(self, can):
        self.can = can
        self.line = []
        self.maxValue=100
        self.minValue=0
        self.maxLine=20

        # graphical properties of the lines
        self.linestep = 5
        self.x_limit = 20
        self.y_limit = 250

    def setMaxValue(self, max):
        self.maxValue = max

    def getMaxValue(self):
        return self.maxValue

    def setMinValue(self, min):
        self.minValue = min

    def getMinValue(self):
        return self.minValue

    def setMaxLine(self, max):
        self.maxLine = max

    def getMaxLine(self):
        return self.maxLine

    # intiate the list with special layouts, f. e. center
    def initList(self, xpos=None):
        if xpos == 'center':
            xtemp = self.maxLine * self.linestep
            self.x_limit = int((self.can.winfo_reqwidth() - xtemp)/2)

    def createList(self):
        for i in range(self.maxLine):
            self.line.append(valueLine(self.can))
            self.line[i].setValue(random.randint(self.minValue,self.maxValue))
            self.line[i].setx_pos(i)
            self.line[i].setx_step(self.linestep)
            self.line[i].setx_limit(self.x_limit)
            self.line[i].sety_limit(self.y_limit)
            self.line[i].createLine()

    def deleteList(self):
        for i in range(len(self.line)):
            delEl = self.line.pop()
            delEl.delete()
            del delEl

    def getLineValue(self, pos):
        return self.line[pos].getValue()

    def swapEls(self, pos1, pos2):
        tempSwap = self.line[pos1]
        self.line[pos1] = self.line[pos2]
        self.line[pos2] = tempSwap
        self.line[pos1].move(pos1)
        self.line[pos2].move(pos2)

    def setColour(self, pos, colour):
        self.line[pos] = colour

    def setHighlight(self, pos):
        self.line[pos].highlight('red')

    def setDownlight(self, pos):
        self.line[pos].downlight()
