from math import sqrt
def fibo(n):
       return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

num=int(input("Enter the number of terms to print: "))
for i in range(num):
    print(int(fibo(i)), end=' ')

print()

