class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getfrequency(j):
            a=''
            l = sorted(j)
            for i in l:
                cnt = str(j.count(i))
                if i not in a:
                    a=a+i+cnt
            return a
        
        
        if len(strs) < 1:
            return [[""]]
        else:
            d={}
            k=[]
            for i in strs:
                code = getfrequency(i)
                d.setdefault(code,[]).append(i)
            for i in d:
                k.append(d[i])
            return k
        


 
            
            
        
        