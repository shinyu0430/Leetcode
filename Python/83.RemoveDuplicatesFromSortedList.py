class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def deleteDuplicates(head):
    start = head  
    current = head  
    while current:
        if current.val != start.val: 
            start.next = current  
            start = current  
        current = current.next  
    if start:
        start.next = None 
    return head

