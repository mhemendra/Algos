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

arrA = [4,6,8,9]
arrB = [1,2,3]

print(sortedMerge(arrA,arrB))
