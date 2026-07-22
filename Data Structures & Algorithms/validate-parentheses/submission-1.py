class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets= "{[("
        bracket_pair = {
            ")": "(",
            "]":"[", 
            "}" : "{"
        }

        stack = [] 
        for char in s: 
            if char in opening_brackets:
                stack.append(char)
            
            else: 
                if not stack or stack[-1] != bracket_pair[char]:
                    return False 
                stack.pop() 
    
        return not stack 

            

        