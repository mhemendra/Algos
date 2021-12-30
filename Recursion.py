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

print(totalWaysToClimb(4))
