from tkinter import *

from sortlist import linelist
from bubble import bubble

root = Tk()

can = Canvas(root, height=400, width=600, bg='#000000')

can.pack(expand=True)

l = linelist(can)
l.setMaxLine(100)
l.createList()

b = bubble(can)
b.setList(l)
b.sort()

root.mainloop()
