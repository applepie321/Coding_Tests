# Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/?envType=daily-question&envId=2024-03-06

class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None

    def has_cycle(self, head):
        if not head or not head.next:
            return False

        left = head
        right = head.next

        while right and right.next:
            if left == right:
                return True
            left = left.next
            right = right.next.next

        return False
