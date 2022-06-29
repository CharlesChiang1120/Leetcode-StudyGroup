class Solution:
    # V1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # BigO(n^2)
        # Go through all elements
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]     
                else:
                    pass




    # V2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        
        # calculate target minus elements in nums
        for i in nums:
            hash_table[i] = target - i

        for j in range(0, len(nums)):
            if hash_table[nums[j]] in nums:

                # [3, 2, 4] return [0, 0] so need to pass
                if j == nums.index(hash_table[nums[j]]):
                    pass 
                else:
                    return [j, nums.index(hash_table[nums[j]] )]


    # V3
    def twoSum(self, nums: List[int], target:int) -> List[int]:
            values = {}
            # structure: values{ value:index}
            for idx, element in enumerate(nums):
                check = target-element 
                if check in values:
                   return [values[check], idx]
                else:
                    values[element] = idx
                