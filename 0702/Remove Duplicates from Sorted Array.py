# V1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(i)
            else:
                i = j
                j += 1
            
        return 
