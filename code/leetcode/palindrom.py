from typing import List
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    else:
        rev_x = int(str(x)[::-1]) # [::-1]:文字列の反転
        if rev_x == x:
            return True
        else: 
            return False

x = 123
print(isPalindrome(x))

x = -121
print(isPalindrome(x))

x = 121
print(isPalindrome(x))