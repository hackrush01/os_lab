import os, time

newPid = os.fork()

if(newPid == 0):
    print("Child")
    time.sleep(2)
    print(os.getpid(), newPid)
    print("Child exited")
    os._exit(0)
else:
    print("Parent")
    time.sleep(3)
    print(os.getpid(), newPid)
    print("Parent exited")
    os._exit(0)

