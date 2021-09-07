a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))


if a>b:
    if a>c:
        print("greatest number is ",a)
        if b>c:
            print("second greatest is",b)
        else:
            print("second greatest is",c)
if b>c:
    if b>a:
        print("greatest is",b)
        if a>c:
            print("second greatest is",a)
        else:
            print("second greatest is", c)

else:
    print("greatest is",c)
    if a>b:
        print("second greatest is",a)
    else:
        print("second greatest is",b)


