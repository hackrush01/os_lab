  10:
del list3
list3 = list()
for k in range(total):
    if len(list1) == i:
        list3 += list2[j:]
        break
    elif len(list2) == j:
        list3 += list1[i:]
        break
    elif list1[i] < list2[j]:
        list3.append(list1[i])
        i += 1
    else:
        list3.append(list2[j])
        j += 1
