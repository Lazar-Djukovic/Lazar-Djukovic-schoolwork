nums = [4,5,9,14,3,8,11]

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
             
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key


insertionSort(nums)
print(nums)