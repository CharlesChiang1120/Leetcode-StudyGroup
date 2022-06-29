class Solution:
    def romanToInt(self, s: str) -> int:
        Roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9,'XL':40, 'XC':90, 'CD':400, 'CM':900}
        IV_count = IX_count = XL_count = XC_count = CD_count = CM_count = 0
        
        if 'IV' in s:
            IV_count = s.count('IV')
            s = s.replace('IV', '')
        
        if 'IX' in s:
            IX_count = s.count('IX')
            s = s.replace('IX', '')
        
        if 'XL' in s:
            XL_count = s.count('XL')
            s = s.replace('XL', '')
        
        if 'XC' in s:
            XC_count = s.count('XC')
            s = s.replace('XC', '')
        
        if 'CD' in s:
            CD_count = s.count('CD')
            s = s.replace('CD', '')
        
        if 'CM' in s:
            CM_count = s.count('CM')
            s = s.replace('CM', '')
        
        final_sum = 0
        
        for i in s:
            final_sum += Roman_dict[i]
            
        final_sum += IV_count*4
        final_sum += IX_count*9
        final_sum += XL_count*40
        final_sum += XC_count*90
        final_sum += CD_count*400
        final_sum += CM_count*900
        
        return final_sum
        