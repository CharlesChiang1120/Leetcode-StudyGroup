# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        l2_list = []

        while l1 != None:
            l1_list.append(l1.val)
            l1 = l1.next
        
        while l2 != None:
            l2_list.append(l2.val)
            l2 = l2.next

        l1_list = l1_list[::-1]
        l2_list = l2_list[::-1]
        
        l1_str = '' 
        l2_str = ''
        
        for element in l1_list: 
            l1_str += str(element)
         
        for element in l2_list: 
            l2_str += str(element)
            
        final_sum = int(l1_str) + int(l2_str)
        final_sum_str = str(final_sum)[::-1]
        
        final_list = []
        for i in final_sum_str:
            final_list.append(i)
        
        # 兩個指向同一個linked list
        cur = l3 = ListNode()
        
        for e in final_list:
            cur.next = ListNode(e)
            cur = cur.next
        
        return l3.next