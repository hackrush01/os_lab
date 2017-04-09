elements = input("Enter the elements: ").split()
arr = [int(element) for element in elements]

aLen = len(arr)

for i in range(1,aLen):
  key=arr[i]
  j=i-1

  while (j >= 0 and arr[j] > key):
    arr[j+1]=arr[j]
    j=j-1

  arr[j+1]=key

print("Sorted Array Is:    ",end='')

for ar in arr:
    print(ar, end=' ')

print()
