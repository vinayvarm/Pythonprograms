# number=int(input("enter number"))


def oddevenlist(number):
    i = 1
    list1 = []
    list2 = []
    while (i <= number):
        if i % 2 == 0:
            list1.append(i)
            i = i + 1

        elif i % 2 == 1:
            list2.append(i)

            i = i + 1
    print("even numbers are", list1)
    print("odd numbers are", list2)

# oddevenlist(number)

