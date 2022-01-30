import numpy as np

def swapNumbers(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a , b

def checkwon(arr):
    if sum(arr) in (0,3):
        return True

def tictactoe(arr):
    for i in range(0, len(arr)):
        row = arr[i,:].reshape(-1)
        column = arr[:,i].reshape(-1)
        if checkwon(row) or checkwon(column):
            return True
            break

def findsmallestdiffbrute(arr1, arr2):
    smallestdiff = 20000
    #output =[]
    #output.append([0,0])
    for elem1 in arr1:
        for elem2 in arr2:
            diff = elem1 - elem2
            if diff < smallestdiff and diff>=0:
                smallestdiff = diff
                #output.append([elem1, elem2])
    return smallestdiff

def findsmallestdiff(arrA, arrB):
    arrA = sorted(arrA)
    arrB = sorted(arrB)
    smallestDiff = 20000
    indexA = indexB = 0
    while indexA<len(arrA) and indexB<len(arrB):
        elemA = arrA[indexA]
        elemB = arrB[indexB]
        if elemA < elemB:
            diff = elemB - elemA
            indexA += 1
        else:
            diff = elemA - elemB
            indexB += 1
        if diff<smallestDiff:
            smallestDiff=diff
    return smallestDiff


arr1 = [1,15,11,267,88]
arr2 = [3,127,235,19,8]
print(findsmallestdiff(arr1, arr2))

arr= np.ones([3,3])

