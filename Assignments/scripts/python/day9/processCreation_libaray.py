from multiprocessing import Process
import os
import time

def sleeper(name, seconds):
  print("Starting child process with id:", os.getpid())
  print("Parent process:", os.getppid())
  print("Sleeping for %s seconds" %(seconds))
  time.sleep(seconds)
  print("Done Sleeping\n")
  
  return seconds

print("In parent process (id %s)\n" %(os.getpid()))
p = Process(target=sleeper, args=('bob', 2))
p_start = p.start()

print("In parent process after child process start")
print("Parent process about to join child process\n")
p.join()
print("In parent process after child process join")
print("Parent process exiting with id", os.getpid())
print("The parent's parent process:", os.getppid())

