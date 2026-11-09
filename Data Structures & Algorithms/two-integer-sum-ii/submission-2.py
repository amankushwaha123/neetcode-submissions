class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        lst = list()
        while l < r:
            if (numbers[l]+numbers[r] == target):
                    lst.append(l+1)
                    lst.append(r+1)
                    return lst
            elif numbers[l]+numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1

        