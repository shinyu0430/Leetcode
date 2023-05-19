class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Two pointers / Time:O(n),Space:O(1)
# def hasCycle(head):
#     ptr1, ptr2 = head, head
#     while ptr1 and ptr1.next:
#         ptr1 = ptr1.next
#         ptr2 = ptr2.next.next
#         if (ptr1 == ptr2):
#             return True
#     return False


# Set / Time:O(n),Space:O(n)
def hasCycle(head):
    setTemp = set()
    while (head):
        if head.next in setTemp:
            setTemp.add(head.next)
        else:
            return False
        head = head.next
    return False


def createLinkedList(nums):
    head = None
    cur = head
    for node in nums:
        if head is None:
            head = ListNode(node)
            cur = head
        else:
            cur.next = ListNode(node)
            cur = cur.next
    return head


print(hasCycle(createLinkedList([1, 2])))
