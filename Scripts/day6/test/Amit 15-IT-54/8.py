from math import sqrt

num = int(input("Enter a POSITIVE number: "))
result = sqrt(num)

print("Square root of {0:d} upto 5 decimal places is: {1:.5f}".format(num, result))
