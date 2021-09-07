def div(a,b):
    c=int(a/b)
    print(c)
try:
    div(20, 0)
    print(d)
except ZeroDivisionError :
    print("cannot devide by zero")
except NameError:
    print("handles name exception")
finally:
    print("this line will be exectued")




