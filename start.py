from tkinter import *
import random

from sortlist import valueLine

root = Tk()

can = Canvas(root, height=400, width=600, bg='#000000')

can.pack(expand=True)

line = valueLine(can)
line.setValue(100)
line.setx_pos(0)
line.setx_step(5)
line.setx_limit(20)
line.sety_limit(250)
line.createLine()

root.mainloop()
