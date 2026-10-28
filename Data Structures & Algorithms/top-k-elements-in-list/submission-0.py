class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max = 0
        d={}
        l=[]
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        e = sorted(d.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            l.append(e[i][0])
        return l




            

        

        