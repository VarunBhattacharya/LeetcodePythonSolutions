# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root):
        #Approach 1 - BFS Approach - Time Complexity - O(2*height) and Space Complexity - O(N)
        '''
        if not root:
            return
        queue = [root]
        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                currNode = queue.pop(0)
                level.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            res.append(level)
        return res[::-1]
        '''

        #Approach 2 - DFS Approach - Time Complexity - O(2*height) and Space Complexity - O(N)
        res = []
        def dfs(root, level):
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                dfs(root.left, level+1)
            if root.right:
                dfs(root.right, level+1)
        if root:
            dfs(root, 0)
        return res[::-1]

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrderBottom(root))