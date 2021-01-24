import numpy as np
def sudokuChecker(newArray):
    for i in range(newArray.shape[0]):
        rowflag = checkDuplicates(newArray[i,:])
        if not (rowflag):
            return False
        colFlag = checkDuplicates(newArray[:, i])
        if not (colFlag):
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            squareFlag = checkDuplicates(newArray[j:j+3,i:i+3].reshape(-1))
            if not squareFlag:
                return False
    return True

def checkDuplicates(numbers):
    print(numbers.shape)
    numCount = {}
    for num in numbers:
        if num!=0:
            numCount.setdefault(num,0)
            numCount[num]+=1
    for key in numCount:
        if numCount[key] > 1:
            return False
    return True

if __name__ =='__main__':
    #newArray = np.random.randint(1, 10, size=(9, 9))
    string="3 0 6 5 0 8 4 0 0 5 2 0 0 0 0 0 0 0 0 8 7 0 0 0 0 3 1 0 0 3 0 1 0 0 8 0 9 0 0 8 6 3 0 0 5 0 5 0 0 9 0 6 0 0 1 3 0 0 0 0 2 5 0 0 0 0 0 0 0 0 7 4 0 0 5 2 0 6 3 0 0"
    inputArray = np.array(string.split(" ")).astype(int).reshape(9,-1)
    print(inputArray)
    isValidSudoku = sudokuChecker(inputArray)
    print(isValidSudoku)