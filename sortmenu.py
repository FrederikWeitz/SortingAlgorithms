from tkinter import *
from tkinter.font import *

class sortmenu():

    def __init__(self, can):
        self.can = can

        menufont = Font('Helvetica', 12)
        
        self.callelements()


    def callelements(self):
        self.startsort = Button(can, bg='black', bd=1, fg='white', font=menufont,
                                activebackground='#222222', text='sort', width=6)
        self.startSortButton = self.can.create_window(30, 30, window=self.startsort)
