from tkinter import *
window=Tk()
window.title("Entry Widget for Output")
content=StringVar()
entOutput=Entry(window,state="readonly",textvariable=content)
entOutput.grid(padx=100,pady=15)
content.set("Hello World!")
window.mainloop()
