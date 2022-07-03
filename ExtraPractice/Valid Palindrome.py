class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for i in s.lower():
            if i.isalnum():
                s_list.append(i)

        return s_list == s_list[::-1]
