class Solution:
    def climbStairs(self, n: int) -> int:
        # V1
#         if n == 1:
#             return 1
        
#         elif n == 2:
#             return 2
        
#         else:
#             return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        # V2
        if n == 1:
            return 1

        elif n == 2:
            return 2

        else:
            a = 1
            b = 2
            c = 0
            for _ in range(n-2):
                c = a + b
                a = b
                b = c

            return c
