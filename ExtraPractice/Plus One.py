class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:   
        digits_int = int(''.join(str(i) for i in digits))
        digits_int += 1
        digits_list = []
        for i in str(digits_int):
            digits_list.append(int(i))
            
        return digits_list
