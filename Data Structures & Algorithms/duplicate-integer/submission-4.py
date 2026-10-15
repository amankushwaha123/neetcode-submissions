class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) < 1):
            return False
        else:
            s= set()
            for i in nums:
                if i in s:
                    return True
                s.add(i)
            return False
        
       
            