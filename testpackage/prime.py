# number=int(input("enter number"))

def prime(number):
    for i in range(2, number):
        if number % i == 0:
            print("not a prime")
            break
    else:
        print("prime number")


# prime(number)
