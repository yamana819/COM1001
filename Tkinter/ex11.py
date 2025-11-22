from tkinter import *

def sortItems(event):
    liste.sort()
    content.set(tuple(liste))

window=Tk()
window.title("Colors")
liste=["red","orange","yellow","blue"]
content=StringVar()
lstColors=Listbox(window,width=10,height=5,listvariable=content)
lstColors.grid(padx=100,pady=15)
content.set(tuple(liste))
lstColors.bind("<Button-3>",sortItems)
window.mainloop()
