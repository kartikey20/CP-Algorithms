from copy import deepcopy


class ListNode:
    def __init__(self, val):
        self.data = val
        self.next = None


def circular(head: ListNode):
    temp = head

    curr = head
    while curr:
        curr = curr.next
        if curr == temp:
            return True
    return False


head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)

head.next = second
second.next = third
third.next = fourth
fourth.next = head

print(circular(head))
