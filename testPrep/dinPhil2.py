import threading

class acquire(object):
    def __init__(self,*locks):
        self.locks = sorted(locks, key=lambda x: id(x))
    def __enter__(self):
        for lock in self.locks:
            lock.acquire()
    def __exit__(self,ty,val,tb):
        for lock in reversed(self.locks):
            lock.release()
        return False
        

# The philosopher thread
def philosopher(left, right):
    while True:
        with acquire(left,right):
             print threading.currentThread(), "eating"

# The chopsticks
NSTICKS = 5
chopsticks = [threading.Lock() 
              for n in xrange(NSTICKS)]

# Create all of the philosophers
phils = [threading.Thread(target=philosopher,
                          args=(chopsticks[n],chopsticks[(n+1) % NSTICKS]))
         for n in xrange(NSTICKS)]

# Run all of the philosophers
for p in phils:
    p.start()
