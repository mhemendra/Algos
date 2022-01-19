import math
import numpy as np
def generateFibonacci(n,elem = [0,1]):
        if len(elem) <= n:
            sum = generateFibonacci(n-1,elem) + generateFibonacci(n-2,elem)
            elem.append(sum)
            return elem[n]
        else:
            return elem[n]
        #return generateFibonacci(n-1) + generateFibonacci(n-2)

#A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
#steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
def totalWaysToClimb(n):
    if n<0:
        return 0
    if n == 0:
        return 1
    else:
        totalWays = totalWaysToClimb(n-1) + totalWaysToClimb(n-2) + totalWaysToClimb(n-3)
    return totalWays

def totalWaysToClimbArr(n, elem = [0, 1]):
    if n<0:
        return elem[0]
    elif len(elem) <= n:
        totalWays = totalWaysToClimbArr(n-1, elem) + totalWaysToClimbArr(n-2, elem) + totalWaysToClimbArr(n-3, elem)
        elem.append(totalWays)
        return elem[n]
    else:
        return elem[n]

def roboGrid(grid, r, c, path = []):
    print(r,c)
    if (r<0 or c<0 or grid[r,c] == 1):
        return False
    if(r==c==0 or roboGrid(grid,r-1,c, path) or roboGrid(grid,r, c-1, path)):
        #print(path)
        path.append([r,c])
        return True
    return False

def checkMagicIndex(arr):
    arraylen = len(arr)
    magicIndexes = []
    for i in range(0,arraylen):
        if arr[i] == i:
            magicIndexes.append(i)
    return magicIndexes

def checkMagicFast(arr, start, end):
    print(arr[:end+1])
    if (start>end):
        return -1
    mid = int((start + end)/2)

    if (arr[mid] == mid):
        return mid
    leftIndex = min(arr[mid],mid-1)
    left = checkMagicFast(arr, start, leftIndex)
    if left >= 0:
        return left
    print('before right')
    rightIndex = max(arr[mid], mid+1)
    right = checkMagicFast(arr, rightIndex, end)
    return right

def subsetsOfSet(arr, index=0):
    if len(arr) == index:
        return [[]]
    else:
        allSubsets = subsetsOfSet(arr, index+1)
        item = arr[index]
        moreSubSets = []
        for subset in allSubsets:
            newSubset = []
            [newSubset.append(value) for value in subset]
            newSubset.append(item)
            moreSubSets.append(newSubset)
        [allSubsets.append(value) for value in moreSubSets if value not in allSubsets]
    return allSubsets

def recursiveMultiply(a, b):
   bigger = b if b>a else a
   smaller = a if a<b else b
   return recursiveMultiplyOrder(smaller, bigger)

def recursiveMultiplyOrder(small, big):
    if small==0:
        return 0
    elif small==1:
        return big
    else:
        s = small >> 1 # divide by 2
        halfProd = recursiveMultiplyOrder(s, big)
        if (small%2 ==0):
            return halfProd + halfProd
        else:
            return halfProd + halfProd + big

def towersOfHanoi(numDisks, arrOut, start=1, buffer=2, end=3):
    if numDisks==1:
        arrOut.append([start,end])
        return arrOut
    else:
        arrOut = towersOfHanoi(numDisks-1,arrOut, start, end, buffer)
        arrOut = towersOfHanoi(1, arrOut, start, buffer, end)
        arrOut = towersOfHanoi(numDisks-1,arrOut, buffer, start, end)

        return arrOut

def paintFill(row, col, arr=[]):
    if row==0 or col==0:
        return
    else:
        if not (arr.__contains__([row, col])):
            arr.append([row, col])
        paintFill(row-1, col, arr)
        paintFill(row, col-1, arr)
        return arr

grid = np.zeros([4,4])
grid[0,1] = 1
roboGrid(grid, 3, 3)

print()