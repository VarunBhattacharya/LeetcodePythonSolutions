from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root) -> int:
        #Approach 1: Level Order BFS - Time Complexity - O(Height) and Space Complexity - O(N)
        if not root:
            return 0

        res = []
        q = deque([root])

        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(sum(level))

        maxVal = float("-inf")
        maxInd = -1
        for ind, val in enumerate(res):
            if val > maxVal:
                maxVal = val
                maxInd = ind
        return maxInd+1

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)
    print(Solution().maxLevelSum(root))