class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i =0
        while (i<len(nums)-2):
            # if first element is +ve then we can not get 0 so break the looop
            if nums[i] > 0:
                break
            # handling left duplicate vale 
            if i>0 and nums[i] == nums[i-1]:
                i += 1
                continue
            l = i+1
            r = len(nums)-1 
            while l < r:
                if nums[i]+nums[l]+nums[r] > 0:
                    r -= 1
                elif nums[i]+nums[l]+nums[r] < 0:
                    l += 1
                else:
                    lst = [nums[i],nums[l],nums[r]]
                    res.append(lst)
                    l += 1
                    r -= 1
                    # handles right duplicate value
                    while nums[r]==nums[r+1] and l<r:
                        r -= 1
            i += 1
        return res
# Final result: [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1], [-1, 0, 1]]
        