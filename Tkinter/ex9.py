from tkinter import *
window=Tk()
window.title("Colors")
liste=["red","blue","pink","orange"]
content=StringVar()
lstColors=Listbox(window,width=10,height=5,listvariable=content)
lstColors.grid(padx=100,pady=15)
content.set(tuple(liste))
window.mainloop()
