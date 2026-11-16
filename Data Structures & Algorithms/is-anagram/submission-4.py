class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = [0]*26
        t_hash = [0]*26
        if (len(s) != len(t)) or (len(s) < 1 or len(t) < 1):
            return False
        else:
            for i in range(len(s)):
                indx_s = ord(s[i])-ord('a')
                s_hash[indx_s] += 1
                indx_t = ord(t[i]) - ord('a')
                t_hash[indx_t] += 1
            if t_hash == s_hash:
                return True
            else:
                return False
            




        
        