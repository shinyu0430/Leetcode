def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    curA, curB = headA, headB

    while curA != curB:
        curA = curA.next if curA else headB
        curB = curB.next if curB else headA
    return curA
