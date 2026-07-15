class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res= False
        containSS={}
        containST={}
        for char in s:
            containSS[char]=containSS.get(char,0)+1
        for char in t:
            containST[char]=containST.get(char,0)+1
        if containSS == containST:
            res=True
        return res
