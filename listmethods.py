
# type(list): It returns the class type of an object.
# append(): Adds a single element to a list.
# extend(): Adds multiple elements to a list.




# list(seq): Converts a tuple into a list.
# cmp(list1, list2): It compares elements of both lists list1 and list2.

# sort(): Sorts the list in ascending order.


list1=[23,45,37,19,30]
list2=["vinay","vijay","vikram","siva"]
list1.sort()
print(list1)
print("+++++++++++++++++++++++++++++")

# index(): Returns the first appearance of the specified value.
print(list2.index('vinay'))
print(list2.index('siva'))
print(list1.index(30))
print("++++++++++++++++++++++++++++")
# max(list): It returns an item from the list with max value.

print("max of list is",max(list1))
print("++++++++++++++++++++++++++++++")

# min(list): It returns an item from the list with min value.
print("minimum of list is",min(list1))
print("++++++++++++++++++++++++++++++")
# len(list): It gives the total length of the list.

print("len of list is",len(list1))
print("++++++++++++++++++++++++++++++")

# converting tuple into list
list()
numb=(34,56,78,90)
print(numb)

print(list(numb))
print("**********************")
# # comparision function
#
# num1=56
# num2=67
# print(cmp(num1,num2))
# print(cmp(num2,num1))
# print(cmp(num1,num1))
# print(cmp(num2,num2))



dict={"a":5,"b":6,"b":10, "b":78,"c":"varma"}
print(dict["c"][2])
print(dict("b"))