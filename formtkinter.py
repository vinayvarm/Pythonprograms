import tkinter

import mysql
import mysql.connector

window=tkinter.Tk()
label=tkinter.Label(window,text="Enter Firstname")
label.pack()
entry1=tkinter.Entry(window)
entry1.pack()
label=tkinter.Label(window,text="Enter Lastname")
label.pack()
entry2=tkinter.Entry(window)
entry2.pack()
label=tkinter.Label(window,text="Enter Email")
label.pack()
entry3=tkinter.Entry(window)
entry3.pack()
label=tkinter.Label(window,text="Enter Mobile")
label.pack()
entry4=tkinter.Entry(window)
entry4.pack()

def dskapp():
    print("button pressed")
    firstname=entry1.get()
    print(firstname)
    lastname = entry2.get()
    print(lastname)
    email = entry3.get()
    print(email)
    mobile = entry4.get()
    print(mobile)
    mydb = mysql.connector.connect(host="localhost", user="root", password="NJDRD@90", port=3306, database="rasadb")
    cursor = mydb.cursor()
    cursor.execute(
        f'insert into new(firstname,lastname,email,mobile) values("{firstname}","{lastname}","{email}","{mobile}");')
    mydb.commit()


butt=tkinter.Button(window,text="submit",command=dskapp)
butt.pack()


window.mainloop()