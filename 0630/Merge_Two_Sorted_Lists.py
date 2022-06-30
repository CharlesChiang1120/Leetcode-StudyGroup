# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        l2_list = []

        while list1 != None:
            l1_list.append(list1.val)
            list1 = list1.next
        
        while list2 != None:
            l2_list.append(list2.val)
            list2 = list2.next

        l1_list.extend(l2_list)
        l1_list.sort()
        
        cur = l3 = ListNode()
        
        for e in l1_list:
            cur.next = ListNode(e)
            cur = cur.next
        
        return l3.next
