# Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=daily-question&envId=2024-03-03

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def remove_nth_from_end(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            second = second.next

        while second is not None:
            first = first.next
            second = second.next

        first.next = first.next.next

        return dummy.next
