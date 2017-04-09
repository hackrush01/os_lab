import multiprocessing


def add(x, y):
    print("Sum is: ", x + y)

def sub(x, y):
    print("Difference is: ", x - y)

def mul(x, y):
    print("Multiplication is: ", x * y)

def div(x, y):
    print("Division is: {0:.4f}".format(x / y))

procs = 4   # Number of processes to create

# Create a list of jobs and then iterate through
# the number of processes appending each process to
# the job list 
jobs = []

processList = [add, sub, mul, div]

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print()

for i in range(0, procs):
    process = multiprocessing.Process(target=processList.pop(), 
                              args=(num1, num2))
    jobs.append(process)

# Start the processes (i.e. calculate the random number lists)      
for j in jobs:
    j.start()

# Ensure all of the processes have finished
for j in jobs:
    j.join()

