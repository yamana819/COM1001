from tkinter import *

def convertToUpperCase(event):
    content.set(content.get().upper())

window=Tk()
window.title("Entry Widget")
content=StringVar()
entName=Entry(window,textvariable=content)
entName.grid(padx=100,pady=15)
entName.bind("<Button-3>",convertToUpperCase)
window.mainloop()
