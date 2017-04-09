import os, time


def add(a, b):
	print("Sum is:", a+b)


def sub(a, b):
	print("Diff is: ", a-b)


def mul(a, b):
	print("Multiplication is:", a*b)


def div(a, b):
	print("Division is:",a/b)


x = int(input("Enter x: "))
y = int(input("Enter y: "))

for i in range(1,5):
    newPid = os.fork()
    if(newPid == 0 and i == 1):
        add(x, y)
    elif(newPid == 0 and i == 2):
        sub(x,y)
    elif(newPid == 0 and i == 3):
        mul(x, y)
    elif(newPid == 0 and i == 4):
        div(x, y)

#if(newPid == 0):
 #   add(x, y)    
  #  sub(x, y)
   # mul(x, y)
    #div(x, y)
#else:
    #print("Parent")
  #  time.sleep(3)
   # print(os.getpid(), newPid)
   # print("Parent exited")
os._exit(0)

