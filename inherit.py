
class A:

    def prime(self,number):
        for i in range(2, number):
            if number % i == 0:
                print("not a prime")
                break
        else:
            print("prime number")

class B(A):
    def oddevenlist(self,number):
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


obj=A()
obj.prime(23)
obj1=B()
obj1.oddevenlist(33)
obj1.prime(45)
