#I have looked at several methods to do this task.
#this is an interesting approach.

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        return prev