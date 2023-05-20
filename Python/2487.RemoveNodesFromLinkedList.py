# Solution1: Monotonic Stack / Time:O(n) / Space:O(n)
def removeNodes(self, head: ListNode) -> ListNode:
    ms, cur = [], head
    while cur:
        while ms and cur.val > ms[-1].val:  # remain top of stack is smallest
            ms.pop()
        ms.append(cur)
        cur = cur.next

    for i in range(len(ms)-1):
        ms[i].next = ms[i+1]

    return ms[0]

# Solution2: DFS / Time:O(n) / Space:O(n)
def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next:
        return head
    nextNode = self.removeNodes(head.next)  # recursive
    if head.val < nextNode.val:
        return nextNode
    else:
        head.next = nextNode
        return head
