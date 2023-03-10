import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head):
        self.head = head

    def getRandom(self) -> int:
        cnt = 0
        res = None
        temp = self.head

        while temp:
            cnt += 1
            if random.randint(1, cnt) == 1:
                res = temp.val
            temp = temp.next

        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    obj = Solution(head)
    param_1 = obj.getRandom()
    print(param_1)