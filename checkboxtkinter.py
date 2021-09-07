import tkinter

window=tkinter.Tk()
def click():

    print(variable.get())
    if variable.get()==1:
        print("u have selected cricket")
    else:
        print("unchecked cricket")

    if variable1.get()==1:
        print("u have selected fifa")
    else:
        print("unchecked fifa")

    if variable2.get() == 1:
        print("u have selected badminton")
    else:
        print("unchecked badminton")


variable=tkinter.IntVar()
checkbutton=tkinter.Checkbutton(window,text="CRICKET",onvalue=1,offvalue=0,variable=variable,command=click)
checkbutton.pack()
variable1=tkinter.IntVar()
checkbtn=tkinter.Checkbutton(window,text="Fifa",onvalue=1,offvalue=0,variable=variable1,command=click)
checkbtn.pack()
variable2=tkinter.IntVar()
checkbad=tkinter.Checkbutton(window,text="Badminton",onvalue=1,offvalue=0,variable=variable2,command=click)
checkbad.pack()

def click1():
    print(variable3.get())
    if variable3.get()==1:
        print("selected boxing")
    else:
        print("selected karate")


variable3=tkinter.IntVar()
radiobtn=tkinter.Radiobutton(window,text="boxing",value=1,variable=variable3,command=click1)
radiobtn.pack()
radiobtn1=tkinter.Radiobutton(window,text="karate",value=2,variable=variable3,command=click1)
radiobtn1.pack()

window.mainloop()