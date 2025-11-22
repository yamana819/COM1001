from tkinter import *

def changeBackgroundColor(event):
    lstColors["bg"]=lstColors.get(lstColors.curselection())

window=Tk()
window.title("Colors")
liste=["red","blue","orange","yellow"]
content=StringVar()
lstColors=Listbox(window,width=10,height=5,listvariable=content)
lstColors.grid(padx=100,pady=15)
content.set(tuple(liste))
lstColors.bind("<<ListboxSelect>>",changeBackgroundColor)
window.mainloop()

