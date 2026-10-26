class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for s in strs:   #O(n)
            counts = [0] * 26
            for ch in s:                       # O(k)
                counts[ord(ch) - ord('a')] += 1
            key = tuple(counts)                # tuples are hashable, lists aren't
            d.setdefault(key, []).append(s)
        return list(d.values())
        


 
            
            
        
        