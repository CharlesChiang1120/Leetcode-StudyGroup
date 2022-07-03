class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        else:
            substring_list = []
            for j in range(0, len(s)):
                substring = ''
                substring += s[j]
                for i in range(j+1, len(s)):
                    if s[i] not in  substring:
                        substring += s[i]
                    else:
                        break

                substring_list.append(substring)

            return len(max(substring_list, key=len))
