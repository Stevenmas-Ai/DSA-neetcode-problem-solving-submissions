class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        i=0
        j=len(s)-1

        while i < j:
            if s[i] == s[j]:
               i=i+1
               j=j-1
            else:
               return False
        return True