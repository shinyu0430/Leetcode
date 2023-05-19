class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(self, head):
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
    median = (length//2)+1

    cur = head
    for i in range(1, median+1):
        if (i == median):
            return cur
        cur = cur.next
