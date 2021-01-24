def isPalindrome(testString):
    dict = {}
    for c in testString.lower():
        dict.setdefault(c, 0)
        dict[c] = dict[c] + 1
    isOdd=0
    for key in dict:
        if(dict[key]%2!=0):
            if (isOdd == 1):
                return False
            else:
                isOdd+=1
    print(isOdd)
    return True

if __name__ =='__main__':
    testString = "Mlaalm"
    output = isPalindrome(testString)
    if(output):
        print('The string is a palindrome')
    else:
        print('Not a palindrome')