def mergesort(array):
    if len(array)>1:
        middle = len(array)//2
        left = array[:middle]
        right = array[middle:]
        mergesort(left)
        mergesort(right)
        helperLeft = helperRight = current = 0
        while (helperLeft < len(left) and helperRight < len(right)):
            if (left[helperLeft] < right[helperRight]):
                array[current] = left[helperLeft]
                helperLeft += 1
            else:
                array[current] = right[helperRight]
                helperRight += 1
            current += 1
        """The below loops are used for the remaining elements ie for [1,4] and [2,3]
        above loop will compare 1,2 then 4,2 and finally 4,3 and adds the smallest one to array
        now the left, right becomes [4] and [] now above loop fails as right condition fails.
        Also needed for unequal elements in left and right."""
        while(helperLeft < len(left)):
            array[current] = left[helperLeft]
            helperLeft += 1
            current += 1
        while(helperRight < len(right)):
            array[current] = right[helperRight]
            helperRight += 1
            current += 1
def partition(array, low, high):
    #pivot with last element(can be any), ie this element will be placed in the correct sorted location
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if(array[j]<= pivot):
            i += 1
            #elements less than pivot are swapped to be before i
            array[i], array[j] = array[j], array[i]
    #now all the elements less than pivot are till i, now place the pivot(arr[high]) in i+1
    #which is the correct sorted place
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quickSort(array, low, high):
    if(low<high):
        partVal = partition(array, low, high)
        quickSort(array, low, partVal-1)
        quickSort(array, partVal+1, high)

arr= [2,3,5,4,66,1,6]
high = len(arr)-1

quickSort(arr, 0, high)
print(arr)
