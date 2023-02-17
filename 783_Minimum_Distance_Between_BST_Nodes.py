# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root) -> int:
        #Approach 1 - Naive Method - Time Complexity - O(N) and Space Complexity - O(1)
        res = []
        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        res.sort()
        minDiff = float('inf')
        for i in range(1, len(res)):
            minDiff = min(minDiff, res[i] - res[i-1])
        return minDiff


        #Approach 2 - DFS - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        prevNode, res = None, float('inf')

        def dfs(node):
            if not node:
                return

            dfs(node.left)            

            nonlocal prevNode, res
            if prevNode:
                res = min(res, node.val - prevNode.val)
            prevNode = node

            dfs(node.right)
        dfs(root)
        return res
        '''

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    print(Solution().minDiffInBST(root))