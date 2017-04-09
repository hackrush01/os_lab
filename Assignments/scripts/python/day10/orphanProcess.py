import os
def child():
    print("In child:", os.getpid())
    print("Its parent ID:",os.getppid())

def parent():
    newpid = os.fork()
    if newpid == 0:
        child()
    print("In parent:",os.getpid())
    os._exit(0)

parent()

