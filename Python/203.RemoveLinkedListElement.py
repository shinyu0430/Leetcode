# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# solution1:two pointer
# def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#     # dummy:to link next,curr:to point current node
#     dummy, curr = None, head
#     while curr:
#         if curr.val == val:
#             if dummy:
#                 dummy.next = curr.next
#             else: #  first is the same
#                 head = curr.next
#         else:
#             dummy = curr
#         curr = curr.next
#     return head

# solution2:one pointer(check the first node at the end)
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    # dummy:to link next,curr:to point current node
    curr = head
    while curr and curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head.next if head and head.val == val else head
