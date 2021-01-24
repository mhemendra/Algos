def getSumOfCubes():
	sumOfCubes = {}
	for num1 in range(1,1001):
		for num2 in range(num1,1001):
			result = num1**3 + num2**3
			sumOfCubes.setdefault(result,[])
			sumOfCubes[result].append([num1,num2])
	return sumOfCubes

def printResults(sumOfCubes):
	for key in sumOfCubes:
		if(len(sumOfCubes[key])>=2):
			print(sumOfCubes[key])


if __name__ == '__main__':
    sumOfCubes = getSumOfCubes()
    printResults(sumOfCubes)