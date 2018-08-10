from tkinter import *
from tkinter.font import *

from sortlist import linelist
from bubble import bubble

class sortmenu():

    def __init__(self, root):
        self.root = root
        
        self.can = Canvas(self.root, height=400, width=600, bg='#000000')
        self.can.pack(expand=True)

        self.menufont = Font(family='Arial', size=10)

        self.list_to_sort = None
        self.sorted = False
        
        self.callelements()


    def callelements(self):
        rect_menu = self.can.create_rectangle(55,55,545,90,outline='white',fill='black')

        BWIDTH = 65 # Konstante für die Aufteilung der Buttons

        self.startsort = Button(self.can, bg='black', bd=1, fg='white', font=self.menufont,
                                activebackground='#222222', activeforeground='white',
                                text='quit', width=6, anchor=N,
                                command=self.quitSort)
        self.startSortButton = self.can.create_window(60 + 0*BWIDTH, 60,
                                                      window=self.startsort, anchor=NW)

        self.startsort = Button(self.can, bg='black', bd=1, fg='white', font=self.menufont,
                                activebackground='#222222', activeforeground='white',
                                text='new', width=6, anchor=N,
                                command=self.newList)
        self.startSortButton = self.can.create_window(60 + 1*BWIDTH, 60,
                                                      window=self.startsort, anchor=NW)
        
        self.startsort = Button(self.can, bg='black', bd=1, fg='white', font=self.menufont,
                                activebackground='#222222', activeforeground='white',
                                text='sort', width=6, anchor=N,
                                command=self.sortList)
        self.startSortButton = self.can.create_window(60 + 2*BWIDTH, 60,
                                                      window=self.startsort, anchor=NW)

    def quitSort(self):
        self.root.destroy()
        
    def newList(self):
        if self.list_to_sort != None:
            self.list_to_sort.deleteList()
        self.list_to_sort = linelist(self.can)
        self.list_to_sort.setMaxLine(30)
        self.list_to_sort.initList(xpos='center')
        self.list_to_sort.createList()
        self.sorted = False

    def sortList(self):
        if self.sorted:
            return
        b = bubble()
        b.setList(self.list_to_sort)
        b.initSort()
        
        def listStep():
            if b.step():
                self.can.after(20, listStep)

        listStep()
        self.sorted = True
