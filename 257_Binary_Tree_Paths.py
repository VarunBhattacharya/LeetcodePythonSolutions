# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):
        #Approach 1: Recursive DFS - Time Complexity - O(Height) and Space Complexity - O(1)
        res = []

        def dfs(root, val):
            val += str(root.val)
            if not root.right and not root.left:
                res.append(val)
                return
            if root.right:
                dfs(root.right, val+"->")
            if root.left:
                dfs(root.left, val+"->")
        
        dfs(root, "")
        return res

        #Approach 2: Iterative DFS - Time Complexity - O(Height) and Space Complexity - O(1)
        '''
        if not root:
            return []
        res = []
        stack = [(root, "")]
        while stack:
            node, val = stack.pop()
            val += str(node.val)
            if not node.right and not node.left:
                res.append(val)
            if node.right:
                stack.append((node.right, val+"->"))
            if node.left:
                stack.append((node.left, val+"->"))
        return res
        '''

        #Approach 3: BFS - Time Complexity - O(Height) and Space Complexity - O(1)
        '''
        if not root:
            return []
        res = []
        queue = [(root, "")]
        while queue:
            node, val = queue.pop(0)
            val += str(node.val)
            if not node.right and not node.left:
                res.append(val)
            if node.right:
                queue.append((node.right, val+"->"))
            if node.left:
                queue.append((node.left, val+"->"))
        return res
        '''


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    sol = Solution()
    print(sol.binaryTreePaths(root))