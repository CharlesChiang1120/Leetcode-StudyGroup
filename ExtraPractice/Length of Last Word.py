class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.split()
        if s:
            return len(s[-1])
        return 0
        
