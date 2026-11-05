class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        mx_cnt=0
        r = 0
        if len(nums) == 1:
            return 1
        else:
            while r<len(nums)-1:
                if nums[r] == nums[r+1]:
                    r += 1
                elif nums[r] == nums[r+1]-1:
                    cnt += 1
                    r += 1
                elif (nums[r] != nums[r+1]-1) and (r < len(nums)-1):
                    cnt = 0
                    r += 1
                if cnt >= mx_cnt:
                    mx_cnt = cnt+1
            

        return mx_cnt
              


        


        