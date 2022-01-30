def kadane(arr):
    sum, maxSum = arr[0], arr[0]
    for elem in arr[1:]:
        sum = max(elem, sum+elem)
        maxSum = max(sum, maxSum)
        print(sum, maxSum)
    return maxSum

arr = [1,2,3,-100,1,3]
print(kadane(arr))
