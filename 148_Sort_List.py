# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        #Using Merge Sort recursively - Time Complexity - O(NlogN) and Space Complexity = O(logN)
        if not head or not head.next: #if no element or only single element
            return head
        
        #split it into two halves
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp

        #sort each halves recursively
        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeList(left, right)
    
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def mergeList(self, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next

if __name__ == "__main__":
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    head = Solution().sortList(head)
    while head:
        print(head.val)
        head = head.next