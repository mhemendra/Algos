import numpy as np
def search(arr, elem):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high+low)//2
        if arr[mid] == elem:
            return mid
        elif arr[mid] > elem:
            high = mid - 1
        else:
            low = mid + 1
    return False

def searchRecursively(arr, elem, low, high):
    if low>high:
        return
    mid = (high + low)//2
    if arr[mid] == elem:
        return mid
    elif arr[mid] > elem:
        return searchRecursively(arr, elem, low, mid-1)
    else:
        return searchRecursively(arr, elem, mid+1, high)

def sortedMerge(arrA, arrB):
    indexA = len(arrA) - 1
    indexB = len(arrB) - 1
    indexMerged = len(arrA) + len(arrB) - 1
    mergedArr = np.empty(indexMerged + 1)

    for elem in range(len(arrA)):
        mergedArr[elem]  = arrA[elem]

    while indexB>=0:
        if indexA>=0 and arrA[indexA] > arrB[indexB]:
            mergedArr[indexMerged] =  arrA[indexA]
            indexA -= 1
        else:
            mergedArr[indexMerged] =  arrB[indexB]
            indexB -= 1
        indexMerged -= 1
    return mergedArr

def searchNoSize(arr,elem):
    i=1
    try:# the Listy should return -1 is out of range
        while not arr[i] == -1:
            if arr[i] > elem:# means the element is before i
                return searchElem(arr, elem, i//2, i)
            i *= 2
    except:
        return searchElem(arr, elem, i//2, i) #if the ith element return -1, there will be some elements after i-10

def searchElem(arr, elem, low, high):
    print(arr, elem, low, high)
    for i in range(low, high):
        try:
            if arr[i] == elem:
                return i
        except:
            return -1

arr = [2,2]
elem = 3

print(searchRecursively(arr, elem,0,2))

arrA = [4,6,8,9]
arrB = [1,2,3]

#print(sortedMerge(arrA,arrB))
