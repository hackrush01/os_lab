from math import sqrt
from time import sleep as ts
import multiprocessing

def fibo(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def print_fibo(num):
    print("Fibonacce series is: ", end='')
    
    for i in range(0, num):
        print(int(fibo(i)), end=' ')

def print_sum(num):
    print("\n\nSum of natural numbers is: ", int(num * (num + 1) / 2))


procs = 2   # Number of processes to create

# Create a list of jobs and then iterate through
# the number of processes appending each process to
# the job list 
jobs = []

processList = [print_sum, print_fibo]

num = int(input("Enter the number: "))

print()

for i in range(0, procs):
    process = multiprocessing.Process(target=processList.pop(), args=(num, ))
    jobs.append(process)

# Start the processes (i.e. calculate the random number lists)      
for j in jobs:
    j.start()
    ts(1)

# Ensure all of the processes have finished
for j in jobs:
    j.join()

