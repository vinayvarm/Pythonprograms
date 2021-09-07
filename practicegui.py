import tkinter
window=tkinter.Tk()
label=tkinter.Label(window,text="hey hi")
label.pack()
entry=tkinter.Entry(window)
entry.pack()

def dskapp():
    print("button pressed")
    data=entry.get()
    print(data)
butt=tkinter.Button(window,text="submit",command=dskapp)
butt.pack()
window.mainloop()