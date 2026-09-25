class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))

#I tried to use split() initially, but that doesn't break individual words out by character. I have to use list() on the string to break it out. 
        