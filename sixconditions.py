num=int(input("enter number"))
a=0
b=1
i=2
while a<b:
    if num % 2 == 0:
        print(num, "is even number")
        a=a+1
        pass
    if num % 2 == 1:
        print(num, "is odd number")
        a = a + 1
        pass
    if num>0:
        div=int(num/10)
        # print(div)
        mul=div*10
        # print(mul)
        rem=num%10
        # print(rem)
        final=div*10+rem
        if final==num:
            print(num,"is a palindrome")
        else:
            print("not a palindrome")



