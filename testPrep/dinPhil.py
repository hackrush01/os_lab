'''
Philosophers table, where five of the great philosophers will be thinking and eating spaghetti.
 
In order for the philosophers not to STARVE they need both the left and right fork to eat.
 
They thing is they can only use the forks on their own immediate left and
right and are not allowed to communicate with each other.
'''
 
from threading import Thread, Semaphore
import random
import time
import Queue
 
 
class Philosopher(Thread):
 
    def __init__(self, name, left_fork, right_fork, waiter):
        super(Philosopher, self).__init__()
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.waiter = waiter
 
    def run(self):
        servings = 0
        while servings <= 3:
            self.waiter.acquire() # acquire the semaphore
            holding_left = self.left_fork.get() # get fork if none blocked until there is one
            holding_right = self.right_fork.get()
            print "%s is eating" % self.name
            servings += 1
            time.sleep(4)                
            self.left_fork.put("Left Fork") # put the fork back in the fork-queue 
            self.right_fork.put("Right Fork")
            self.waiter.release() # release the semaphore
            #time.sleep(0.1) not sure if using a small sleep breaks the rules
 
 
def SetTheTable(guests, waiter):
    left_q = Queue.Queue() # using a queue to represent each fork
    left_q.put("fork")
    wrap_fork = left_q 
    right_q = Queue.Queue()
    right_q.put("fork")
    table = list()
    while philosophers:
        name = random.choice(philosophers)
        philosophers.pop(philosophers.index(name))
        thinker = Philosopher(name, left_q, right_q, waiter)
        left_q = right_q
        if len(philosophers) == 0:
            right_q = wrap_fork
        else:
            right_q = Queue.Queue()
            right_q.put("fork")
        table.append(thinker)
    return table
 
 
if __name__ == '__main__':
    philosophers = ["Plato", "Descartes", "Kant", "Locke", "Hobbes"]
    waiter = Semaphore(4) # create a semaphore with initial value of 4
    seated_guests = SetTheTable(philosophers, waiter)
    for guest in seated_guests:
        guest.start()
