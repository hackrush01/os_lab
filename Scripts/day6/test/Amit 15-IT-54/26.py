def sum(n):
    if n <= 1:
        return n
    else:
        return (sum(n - 1) + n)


terms = int(input("Enter no of terms: "))
print ("The sum is:", sum(terms))
