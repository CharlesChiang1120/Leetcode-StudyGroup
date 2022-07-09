class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # list只有一個數字的時候([0] [1])
        # 然後 n = 0 or 1
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n ==1 :
            return True
        
        elif len(flowerbed) == 1 and flowerbed[0] == 1 and n ==1 :
            return False
        
        # 兩個兩個做判斷
        # 連續兩個數做OR Bitwise 
        # 如果做OR的結果為0
        # 看前面那個bit是否為0 是的話 就直接種樹
        # 要注意一開始如果是兩個0
        # 跟list最後是否為兩個0
        else:
            for i in range(0, len(flowerbed)-1):
                if (flowerbed[i] | flowerbed[i+1]) == 0:
                    if flowerbed[i-1] != None and flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        n -= 1 
        
                    elif i == 0 and flowerbed[i] == 0:
                        flowerbed[i] = 1
                        n -= 1 
             
                    elif i+1 == len(flowerbed)-1 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1 
                else:
                    pass
            
        return n <= 0
