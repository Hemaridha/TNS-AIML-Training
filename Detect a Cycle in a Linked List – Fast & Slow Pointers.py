class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

head.next = node2
node2.next = node3
node3.next = node4

node4.next = node2

print(has_cycle(head))
