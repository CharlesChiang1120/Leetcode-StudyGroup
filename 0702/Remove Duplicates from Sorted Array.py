# V1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if i == 0 and j == 0:
                j += 1
            else:
                if nums[i] == nums[j]:
                    nums.pop(i)
                else:
                    i = j
                    j += 1
            
        return 
