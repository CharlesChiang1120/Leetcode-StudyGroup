# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
# V1 Algorithm       
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
                
            return True
        
        except:
            return False

# V2        
        def hasCycle(self, head: ListNode) -> bool:
            
            while head: 
                if head.val == 'Flag':
                    return True
                elif head.val != 'Flag' :
                    head.val = 'Flag'
                head = head.next
                
            return False
