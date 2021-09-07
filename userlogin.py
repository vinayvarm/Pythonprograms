username="vikram"
password="dell@90"

name=input("enter username ")


if username==name:
    print("please enter password")
    passw=input("enter password ")
    if password==passw:
        print("welcome back",username)
    else:
        print("password is wrong,enter correct password")

else:
    print("please enter correct username")