#  Middle of the Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution class with the main logic
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow  # This is the middle node

# Helper: Create linked list from a Python list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper: Print linked list from a node
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next

# ----------- Test the code locally -----------
if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]  # You can change this list for other tests
    head = create_linked_list(values)

    sol = Solution()
    middle = sol.middleNode(head)

    print("Linked list starting from middle node:")
    print_linked_list(middle)
