import os


def child():
    print("\nA new child:", os.getpid())
    os._exit()


def parent():
    while True:
        newpid = os.fork()  # child- > pid=0, parent -> pid>0, error -> pid<0
        print(newpid)
        if newpid == 0:
            child()
        else:
            pids = (os.getpid(), newpid)
            print("parent: {0:d}, child: {1:d}\n".format(pids[0], pids[1]))
            # print(pids)
        reply = input("q for quit / c for new fork: ")

        if reply == 'c':
            continue
        else:
            break


parent()
