class Solution:
    def isPalindrome(self, s: str) -> bool:
        low=s.lower()
        result=""
        for char in low:
            if char.isalnum():
                 result += char.lower()
                   
        if result == result[::-1]:
            return True
        else:
             return False
        

        