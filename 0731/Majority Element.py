class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = round(len(nums) / 2)
        hash_table = {}
        
        for i in nums:
            if i not in hash_table:
                hash_table[i] = 1
            
            else:
                hash_table[i] += 1
        
        max_value = -1
        max_key = -1
        
        for k, v in hash_table.items():
            
            if v >= majority and v > max_value:
                max_value = v
                max_key = k

        return max_key
