def tour(lis, n):
    diffArr = []
    totalDiff = 0
    for input in lis:
        diff = input[0] - input[1]
        diffArr.append(diff)
        totalDiff+=diff
    if n == 1:
        return 0
    elif totalDiff < 0:
        return -1
    else:
        for i in range(n):
            if (diffArr[i]>=0):
                count = 0
                totalDiff = 0
                j=i
                while (count<n):
                    j = j%n
                    diff = diffArr[j]
                    totalDiff+=diff
                    if(totalDiff<0):
                        break
                    j+=1
                    count+=1
                    if(count==n):
                        return i

if __name__ == '__main__': 
    input = [[4, 6],[6,5],[7,3],[4,5]]
    print(tour(input, 4))
