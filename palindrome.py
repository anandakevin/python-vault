def palindrome(string):
    length = len(string)
    for idx, char in enumerate(string):
        if(string[idx] != string[length - 1 - idx]):
            return False
    return True
    

print(palindrome("asd"))