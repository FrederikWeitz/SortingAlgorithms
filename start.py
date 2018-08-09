from tkinter import *

root = Tk()



can = Canvas(root, height=400, width=600, bg='#000000')

can.pack(expand=True)

line = []

for i in range(20):
    line.append(can.create_line(20+i*20,20,20+i*20,60, fill='white', width=3, capstyle=ROUND))

print(len(line), '  -  ', line[0])

root.mainloop()
