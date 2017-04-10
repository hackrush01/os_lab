import os,time

a=int(input())
b=int(input())

newpid=os.fork()

if newpid==0:
    print("sum= ",a+b)
else:
    os.wait()
    newpid2=os.fork()
    if newpid2==0:
        print("diff= ",a-b)
    else:
        os.wait()
        newpid3=os.fork()
        if newpid3==0:
            print("mult= ",a*b)
        else:
            os.wait()
            print("div= ",a/b)
print("finished")

