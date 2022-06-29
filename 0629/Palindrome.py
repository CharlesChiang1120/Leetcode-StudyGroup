class Solution:
    # convert to string
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]


    # insert each digit into list
    # compare list and reverse list
    def isPalindrome(self, x: int) -> bool:
        a = []
        if x < 0:
            return False
        else:
            while x >=  10:
                a.append(x % 10)
                x = x // 10
            a.append(x)
            
            return a == a[::-1]