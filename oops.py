class add:
    pass
class mul:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("object created")
    def multiply(self):
        print(f"multiplication of {self.a} and {self.b} is {self.a * self.b}")

obj=add()
# print(type(obj))
# obj.count=10
# print(obj.count)
# print(isinstance(obj,add))
# mulobj=mul(10,2)
# mulobj.multiply()

class new(mul):
    __name="vinay"
    def __init__(self,e,f):
        super(new, self).__init__(10,2)
        self.e=e
        self.f=f
        print("object created")

    def sub(self,c,d):
        self.c=c
        self.d=d
        print(f"multiplication of {self.c} and {self.d} is {self.c - self.d}")

newobj=new(10,2)
newobj.multiply()
newobj.sub(34,20)
print(newobj._new__name)



