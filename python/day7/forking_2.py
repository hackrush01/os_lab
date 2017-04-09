import os
import time


def counter(count):
    for i in range(count):
        # time.sleep(1)
        print(os.getpid(), i)


for i in range(2):
    newpid = os.fork()
    time.sleep(1)
    # counter(2)
    pids = (os.getpid(), newpid)
    print("parent: {0:d}, child: {1:d}\n".format(pids[0], pids[1]))
