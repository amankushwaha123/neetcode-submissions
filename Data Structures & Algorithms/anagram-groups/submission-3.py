class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for s in strs:   
            counts = [0] * 26
            for ch in s:                       
                counts[ord(ch) - ord('a')] += 1
            key = tuple(counts)                
            d.setdefault(key, []).append(s)
        return list(d.values())
        


 
            
            
        
        