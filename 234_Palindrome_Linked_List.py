# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
        #Naive Approach: Time Complexity - O(N) and Space Complexity - O(1)
        temp = head
        arr = []
        while temp.next is not None:
            arr.append(temp.val)
            temp = temp.next
        arr.append(temp.val)
        return arr == arr[::-1]

if __name__ == '__main__':
    s = Solution()
    ListNode1 = ListNode(1)
    ListNode2 = ListNode(2)
    ListNode3 = ListNode(2)
    ListNode4 = ListNode(1)
    ListNode1.next = ListNode2
    ListNode2.next = ListNode3
    ListNode3.next = ListNode4
    print(s.isPalindrome(ListNode1))