
def allCombinationsString(str, noOfChars=0, output=[]):

    if len(str) == noOfChars:
        return [" "]
    else:
        output = allCombinationsString(str, noOfChars + 1)
        currChar = str[noOfChars]
        tempOutput = []
        for s in output:
            for i in range(0, len(s)):
                appendedStr = s[:i] + currChar + s[i:]
                tempOutput.append(appendedStr)
        output = tempOutput
        return output

def get_perms_2(string):
    result = []
    get_perms_inner_2(" ", string, result)
    return result

def get_perms_inner_2(prefix, remainder, result):
    if len(remainder)==0:
        result.append(prefix)
    length = len(remainder)
    for i in range(length):
        before = remainder[:i]
        after = remainder[i + 1 :]
        c = remainder[i]
        get_perms_inner_2(prefix + c, before + after, result)


def print_perms(string):
    result = []
    letter_count_map = build_freq_table(string)
    print_perms_inner(letter_count_map, "", len(string), result)
    return result


# returns dictionary <string, integer>
def build_freq_table(string):
    letter_count_map = {}
    for letter in string:
        if letter not in letter_count_map:
            letter_count_map[letter] = 0
        letter_count_map[letter] += 1
    return letter_count_map


def print_perms_inner(letter_count_map, prefix, remaining, result):
    if remaining==0:
        result.append(prefix)
    for character in letter_count_map:
        count = letter_count_map[character]
        if count > 0:
            print(character, count)
            letter_count_map[character] -= 1
            print_perms_inner(
                letter_count_map, prefix+character, remaining - 1, result
            )
            letter_count_map[character] = count
    print('Out', prefix+character)

print(print_perms('aab'))
