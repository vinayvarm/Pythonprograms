# file=open("output.txt","a")
# file.write("hi vinay how are u\n")
# file.write("hi iam fine")
# file.close()
# file=open("output.txt","r")
# rd=file.read(12)
# print(rd)
# md=file.read(6)
# print(md)
# lines=file.readlines()
# print(lines)

file=open("output.txt","r")


rd=file.readlines()
print(rd)

for i in rd:
    new=i.split(",")

    print(type(new))





#
# for i in rd:
#     print("username is ",i)
# print(rd)
