import functools

# list1=[56,34,88,45]
# list2=[]
# for i in list1:
#     num=i*5
#     print(num)
#     list2.append(num)
# print(list2)
#     # list1=list1.append(num)
#
# # print(list1)

list1=[22,33,44,55]
# def mapred(name):
#     return name*5
# print(list(map(mapred,list1)))

def evenodd(number):
    if number%2==0:
        return True
    else:
        return False
print(list(filter(evenodd,list1)))

list2=[88,99,56,44]

print(functools.reduce(lambda a,b:a+b,list2))


