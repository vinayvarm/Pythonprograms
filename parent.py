from testpackage.evenodd import *
from testpackage.prime import *
from testpackage.sum import *
from testpackage.loginfunclist import *
login(name,psw)


print("please choose below options")
print("1.even number\n2.prime number\n3.list of odd and even\n4.exit")
choice = int(input("enter number of ur choice"))
print("dear user ur choice is", choice)



def allmethods():
    if choice == 1:

        even(number)
    elif choice == 2:

        prime(number)
    elif choice == 3:

        oddevenlist(number)

    else:
        print("exit u are of session")

# even(number)
# prime(number)
# oddevenlist(number)
