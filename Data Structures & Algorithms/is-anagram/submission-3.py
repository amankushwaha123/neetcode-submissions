class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) < 1 or len(t) < 1):
            return False
        else:
            return sorted(s) == sorted(t)

