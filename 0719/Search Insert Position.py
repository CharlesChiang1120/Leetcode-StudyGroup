class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            mid = len(nums) // 2
            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                for value in nums[mid+1:]:
                    if target == value:
                        return nums.index(value)

            elif target < nums[mid]:
                for value in nums[:mid]:
                    if target == value:
                        return nums.index(value)
                    
        else:
            if target < nums[0]:
                return 0
            elif target > nums[-1]:
                return len(nums)
            else:
                for i in range(len(nums)):
                    if nums[i] < target and nums[i+1] > target:
                        return i+1
