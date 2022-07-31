class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # value = 0
        # for i in range(0, len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j]-prices[i] > value:
        #             value = prices[j]-prices[i]
        #         else:
        #             pass
        # return value
        left = 0
        right = 1
        max_value = 0
        
        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
            else:
                max_value = max(max_value, prices[right]-prices[left])
            right += 1
                
        return max_value
