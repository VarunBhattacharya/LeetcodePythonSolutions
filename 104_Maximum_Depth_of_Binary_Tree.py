from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root) -> int:
        '''
        #Recursive DFS
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        '''
        
        '''
        #Iterative DFS
        '''
        '''
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res
        '''
        
        
        
        '''
        #Iterative BFS - Level Order Traversal
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return len(res)
        '''

        #Approach 1: Time Complexity - O(Height) and Space Complexity - O(N)
        if not root:
            return 0
        
        res = 0
        q = deque([root])

        while q:
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res += 1
        
        return res

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    print(s.maxDepth(root))