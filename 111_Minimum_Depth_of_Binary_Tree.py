from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root) -> int:
        #Approach 1: Level Order Traversal BFS - Time Complexity - O(Height) and Space Complexity - O(N)
        if not root:
            return 0

        res = []
        q = deque([(root, 1)])

        while q:
            node, depth = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        
        return 0

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(10)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.minDepth(root))