class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pd , zc = 1,0
        for i in nums:
            if i:
                pd *= i
            else:
                zc += 1
        if zc > 1:
            rs = [0]*len(nums)
            return rs
        rs = [0]*len(nums)
        for i,c in enumerate(nums):
            if zc:
                if c:
                    rs[i] = 0
                else:
                    rs[i] = pd
            else:
                rs[i] = pd//c
        return rs



        