# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root) -> bool:
        #Approach 1: DFS - Time Complexity - O(N^2) and Space Commplexity - O(1)
        '''
        def dfs(root):
            if not root:
                return 0
            return 1 + max(dfs(root.left), dfs(root.right))
        if not root:
            return True
        return (abs(dfs(root.left) - dfs(root.right)) <= 1 and
                self.isBalanced(root.left) and self.isBalanced(root.right))
        '''

        #Approach 2: DFS (Top-Down Approach) - Time Complexity - O(N) and Space Commplexity - O(1)
        '''
        def dfs(root):
            if not root:
                return 0
            leftSubTree, rightSubTree = dfs(root.left), dfs(root.right)
            if leftSubTree == -1 or rightSubTree == -1 or abs(leftSubTree - rightSubTree) > 1:
                return -1
            return 1 + max(leftSubTree, rightSubTree)
        return dfs(root) != -1
        '''

        #Approach 3: DFS (Bottom-Up Approach) - Time Complexity - O(N) and Space Commplexity - O(1)
        def dfs(root):
            if not root:
                return [True,0]
            leftSubTree, rightSubTree = dfs(root.left), dfs(root.right)
            diff = (leftSubTree[0] and rightSubTree[0] and 
                    abs(leftSubTree[1] - rightSubTree[1]) <= 1)
            return [diff, 1+max(leftSubTree[1], rightSubTree[1])]
        return dfs(root)[0]

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().isBalanced(root))