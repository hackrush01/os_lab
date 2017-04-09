import os
import time
List = [10, 20, 30, 40, 50, 60]

Sum = 0
Sub = 0
 
PID = os.fork()

if PID == 0:
  for i in range(len(List)):
    Sum = Sum + List[i]
  print("Value of addition = %d by process with ID: %d" %(Sum, os.getpid()))
elif PID > 0:
  os.wait()
  for i in range(len(List)):
    Sub = Sub - List[i]
  print("Value of subtraction = %d by process with ID: %d" %(Sub, os.getpid()))
else:
  print("Error in process creation")

print("Thank You!")

