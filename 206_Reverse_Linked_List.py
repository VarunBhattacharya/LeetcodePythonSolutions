# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        #Iterative Solution - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        '''

        #Recursive Solution - Time Complexity - O(N) and Space Complexity - O(M)
        '''
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
        '''

        #Recursive Solution - 3 pointer approach - Time Complexity - O(N) and Space Complexity - O(M)
        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                next = cur.next
                cur.next = prev
                return reverse(next, cur)

        return reverse(head, None)


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head = s.reverseList(head)
    while head:
        print(head.val)
        head = head.next