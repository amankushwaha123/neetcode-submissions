class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = 0
        cnt = 0
        for i in nums:
            cn = nums.count(i)
            if(cn > cnt):
                cnt = cn
                num = i
        return num




           

        
        