class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = nums.count(val)
        for i in range(cnt):
            nums.remove(val)
        lng = len(nums)
        return lng
 

    

        

        