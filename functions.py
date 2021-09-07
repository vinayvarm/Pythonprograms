
# def message():
#     print("even number")
#
# num=int(input("enter number"))
#
# if num%2==0:
#     message()
# else:
#     print("odd number")
#
# def multiple_print(number=1):
#     print("helloworld "*number)
#
# multiple_print(3)
# multiple_print(5)
# multiple_print()
# def addtion(a,b):
#     return a-b
#     print("vinay")
# add=addtion(5,6)
# print(add*5)
# print(addtion(b=6,a=3))
# print(addtion(3,5,7))

# name=input("enter username ")
# psw=input("enter password ")

# password=input("enter password")

# def login(username,password):
#     un="vinay"
#     pw="dell"
#     if username==un:
#
#         if password == pw:
#             print("welcome back", username)
#         else:
#             print("wrong password")
#     else:
#         print("wrong username")
#
# login(name,psw)

# def multiple_addition(*a):
#     add=0
#     for i in a:
#
#         add=add+i
#     print("add is ",add)
#
#
#
#
# multiple_addition(6,9,5,3,2,1,7,a=8)

def test(**h):

    for i in h:
        print(i,h[i])
        print("first key of dictionary is",i,"value is",h[i])

test(a=10,b=20,c=40,y=89,u=55)

