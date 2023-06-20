from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root, val: int):
        #Approach 1: Recursive BFS - Time Complexity - O(Height) and Space Complexity -O(N)
        '''
        if not root:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)
        '''

        #Approach 2: BFS - Time Complexity - O(Height) and Space Complexity - O(N)
        if not root or root.val == val:
            return root

        q = deque([root])

        while q:
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                if node.val == val:
                    return node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(8)
    print(s.searchBST(root, 2))