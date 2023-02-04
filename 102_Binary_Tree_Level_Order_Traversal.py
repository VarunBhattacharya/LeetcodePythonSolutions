# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        #BFS Algorithm - Time Complexity - O(N) and Space Complexity - O(N)
        '''
        if not root:
            return None
        
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
        return res
        '''

        #BFS Algorithm - Time Complexity - O(N) and Space Complexity - O(N)
        '''
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        
        return res
        '''

        #DFS Algorithm - Time Complexity - O(N) and Space Complexity - O(N)
        res = []
        def dfs(node, level):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
        if root:
            dfs(root, 0)
        return res

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrder(root))