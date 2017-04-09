import os
import time

MAX_COUNT = 5
c_PID = os.fork()
pid = os.getpid()

for i in range(MAX_COUNT):
  print("This line is from pid %d, Parent PID: %d, value = %d" %(pid, os.getppid(), i))
  print()
  time.sleep(1)

