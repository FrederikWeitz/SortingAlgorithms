from tkinter import *

from sortlist import linelist
from bubble import bubble

root = Tk()

can = Canvas(root, height=400, width=600, bg='#000000')

can.pack(expand=True)

l = linelist(can)
l.setMaxLine(100)
l.initList(xpos='center')
l.createList()

b = bubble()
b.setList(l)
b.initSort()

def listStep():
    if b.step():
        can.after(2, listStep)

listStep()

root.mainloop()


