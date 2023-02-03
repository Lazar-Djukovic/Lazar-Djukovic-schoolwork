def merge(list1, list2):
    result = [0] * (len(list1) + len(list2))
    i = j = k = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result[k] = list1[i]
            i += 1
        else:
            result[k] = list2[j]
            j += 1
        k += 1
    while i < len(list1):
        result[k] = list1[i]
        i += 1
        k += 1
    while j < len(list2):
        result[k] = list2[j]
        j += 1
        k += 1
    return result

# Test the merge function
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge(list1, list2)) # Output: [1, 2, 3, 4, 5, 6, 7, 8]