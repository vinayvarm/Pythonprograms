import threading

def cube(number):
    data=(number*number)
    ans=data*number
    print(ans)

def square(num):
    print(num*num)

if __name__=="__main__":
    thread1=threading.Thread(target=cube,args=(5,))
    thread2=threading.Thread(target=square,args=(2,))
    thread2.start()
    thread1.start()
    thread1.join()
    thread2.join()
    print("done")