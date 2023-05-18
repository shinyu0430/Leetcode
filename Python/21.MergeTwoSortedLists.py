class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self,list1,list2):
        cur = dummy = ListNode() # init to a new ListNode object
        while list1 and list2:
            if list1.val < list2.val: # comapre the val of the current nodes of both list
                cur.next  = list1 # point to list 1
                list1,cur = list1.next,list1 # point to next node of list1 and update cur
            else:
                cur.next = list2
                list2,cur =  list2.next,list2

        if list1 or list2: 
                cur.next = list1 if list1 else list2
        return dummy.next

