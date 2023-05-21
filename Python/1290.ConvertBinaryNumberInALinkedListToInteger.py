# solution1
def getDecimalValue(self, head: ListNode) -> int:
    le = 0
    cur = head
    while cur:
        cur = cur.next
        le += 1

    po = le-1
    sum = 0
    while head:
        sum += head.val * (2**po)
        po = po - 1
        head = head.next
    return sum
# solution2: more clever solution


def getDecimalValue(self, head: ListNode) -> int:
    answer = 0
    while head:
        answer = 2*answer + head.val  # Double dabble:double to shift the binary code
        head = head.next
    return answer
