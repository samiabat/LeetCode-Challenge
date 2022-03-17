from math import ceil
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        arr = list(palindrome)
        get = False
        for i in range(len(arr)//2):
            if arr[i]=="a" or get:
                continue
            else:
                arr[i] = "a"
                get = True
        if not get and len(arr)>1:
            t = ord(arr[-1])+1
            arr[-1] = chr(t)
            return "".join(arr)
        if not get:
            return ""
        return "".join(arr)