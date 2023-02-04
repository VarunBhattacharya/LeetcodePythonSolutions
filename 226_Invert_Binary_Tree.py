import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        #Approach - Recursive DFS
        '''
        if not root: #if no root
            return
        #swap children recusively
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        '''
    
        #Approach - Iterative BFS
        if not root:
            return
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

    def printTree(self,root):
        if not root:
            return
        print(root.val)
        self.printTree(root.left)
        self.printTree(root.right)

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print(Solution().invertTree(root))
    Solution().printTree(root)