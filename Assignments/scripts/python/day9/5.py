import multiprocessing


def sort_list(listToSort, result_q):
    listToSort.sort()
    # result_q['list1'] = list1
    result_q.put(listToSort)


list1 = list(map(int, input("Enter the 1st list: ").split()))
list2 = list(map(int, input("Enter the 2nd list: ").split()))
lists = [list1, list2]

# Create a list of jobs and then iterate through
# the number of processes appending each process to
# the job list 
jobs = []
procs = 2   # Number of processes to create

result_q = multiprocessing.Queue()

for listToSort in lists:
    process = multiprocessing.Process(target=sort_list, args=(listToSort, result_q))
    jobs.append(process)

# Start the processes (i.e. calculate the random number lists)      
for j in jobs:
    j.start()

# Ensure all of the processes have finished
for j in jobs:
    j.join()

list1 = result_q.get()
list2 = result_q.get()


i = j = 0
total = len(list1) + len(list2)

result = list()
for k in range(total):
    if len(list1) == i:
        result += list2[j:]
        break
    elif len(list2) == j:
        result += list1[i:]
        break
    elif list1[i] < list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1

print("\nResultant array is:",result)

