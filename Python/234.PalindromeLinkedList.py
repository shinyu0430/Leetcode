# Solution1:Based on stack
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    st = []
    cur = head

    le = 0
    while cur:
        le += 1
        cur = cur.next

    half, odd_flag = le//2+1, 1
    if le % 2 == 0:
        odd_flag = 0

    count = 1
    if le == 1:
        return True
    while head and count <= le:
        if (count < half):
            st.append(head.val)
        else:
            if odd_flag and count == half:
                head = head.next
            if (st.pop() != head.val):
                return False
                break
        head = head.next
        count += 1
    return True

# Solution2: Based on list reverse


def isPalindrome(self, head: Optional[ListNode]) -> bool:
    look_ls = [head.val]
    cur = head.next
    while cur:
        look_ls.append(cur.val)
        cur = cur.next

    look_ls_2 = look_ls.cpoy()
    look_ls_2.reverse()

    return look_ls == look_ls_2

# Solution3: Based on simple brute force


def isPalindrome(self, head: Optional[ListNode]) -> bool:
    st = []
    while head:
        st.append(head.val)
        head = head.next
    return st == st[::-1]
