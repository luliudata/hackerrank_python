# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
# ref: https://realpython.com/linked-lists-python/
# there’s a specific object in the collections module that you can use for linked lists called deque (pronounced “deck”)
# which stands for double-ended queue.

# from collections import deque


def mergeLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # linked list is sorted already
    # initialize a head node
    # then compare head1 and head2, append the smaller node to the head node
    if head1.data <= head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next

    current = head
    while head1 is not None or head2 is not None:
        if head1 is None:
            current.next = head2
            break
        if head2 is None:
            current.next = head1
            break
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    return head


