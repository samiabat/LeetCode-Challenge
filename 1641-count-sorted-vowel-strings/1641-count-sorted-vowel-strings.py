class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        def count(vowels, n, index, s_len):
            if s_len == n:
                return 1
            if(index >= len(vowels)):
                return 0
            return count(vowels, n, index+1, s_len) + count(vowels, n, index, s_len+1)
        return count(vowels, n, 0, 0)
            
            