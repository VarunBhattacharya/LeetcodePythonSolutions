# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head):
        #Naive Approach: List->Arr->Tree - Time Complexity - O() and Space Complexity - O()
        #convert linked list to arr
        if not head:
            return
        arr = []
        temp = head
        while temp.next is not None:
            arr.append(temp.val)
            temp = temp.next
        arr.append(temp.val)

        #convert arr to bst
        def arrToBST(arr):
            if not arr:
                return None
            mid = len(arr)//2
            node = TreeNode(arr[mid])
            node.left = arrToBST(arr[:mid])
            node.right = arrToBST(arr[mid+1:])
            return node
        return arrToBST(sorted(arr))

    def levelOrder(self, root):
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

if __name__ == "__main__":
    s = Solution()
    ListNode1 = ListNode(-10)
    ListNode2 = ListNode(-3)
    ListNode3 = ListNode(0)
    ListNode4 = ListNode(5)
    ListNode5 = ListNode(9)
    ListNode1.next = ListNode2
    ListNode2.next = ListNode3
    ListNode3.next = ListNode4
    ListNode4.next = ListNode5
    print(s.levelOrder(s.sortedListToBST(ListNode1)))