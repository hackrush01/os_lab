import multiprocessing
from time import sleep as ts


def mul(x, y):
    print("\nMatrix Multiplication is:")
    result = [[0 for x in range(len(X))] for y in range(len(X[0]))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            for k in range(len(X)):
                result[i][j] += X[i][k] * Y[k][j]
            print(result[i][j], end=" ")
        print()


def add(x, y):
    print("\nMatrix Addition is:")
    result = [[0 for x in range(len(X))] for y in range(len(X[0]))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]
            print(result[i][j], end=" ")
        print()


def sub(x, y):
    print("\nMatrix Subtraction is:")
    result = [[0 for x in range(len(X))] for y in range(len(X[0]))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] - Y[i][j]
            print(result[i][j], end=" ")
        print()


# Take input from user
n = int(input('Enter number of elements: '))
X = [[0 for x in range(n)] for y in range(n)]
Y = [[0 for x in range(n)] for y in range(n)]

print("Enter elements of 1st matrix:")
for i in range(n):
    X[i] = list(map(int, input().split()))

print("Enter elements of 2nd matrix:")
for i in range(0, n):
    Y[i] = list(map(int, input().split()))
print()


# Create a list of jobs and then iterate through
# the number of processes appending each process to
# the job list
jobs = []
procs = 3   # Number of processes to create
processList = [add, sub, mul]


for i in range(0, procs):
    process = multiprocessing.Process(target=processList.pop(),
                                      args=(X, Y))
    jobs.append(process)

# Start the processes
for j in jobs:
    j.start()
    ts(1)

# Ensure all of the processes have finished
for j in jobs:
    j.join()
