import numpy as np
print(dir(np))
new=np.array([[[[3,4],[6,9]]]])
print(new)
print(type(new))
print(new.ndim)
print(new.shape)

new1=np.array([[2,3],[5,6]])
new2=np.array([[5,7],[7,9]])
output=np.dot(new1,new2)
print(output)
np.savetxt("output.txt",output,delimiter=",")
