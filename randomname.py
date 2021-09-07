import random
names=input('enter names seperated by commas ')
new=names.split(",")
print(new)



num_items=len(new)
print(num_items)

randomchoice=random.randint(0,num_items-1)
print(randomchoice)

person=new[randomchoice]
print(person + 'is going to pay the bill')

#
# new=random.randint(0,length-1)
# print(new)

