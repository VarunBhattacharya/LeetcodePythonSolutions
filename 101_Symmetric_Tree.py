# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root) -> bool:
        #Approach 1: Recursion - Time Complexity - O(Height) and Space Complexity - O(1)
        if not root:
            return True

        def checkSym(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return (t1.val == t2.val) and checkSym(t1.left, t2.right) and checkSym(t1.right, t2.left)

        return checkSym(root, root)

        #Approach 2: Iteration - Time Complexity - O(Height) and Space Complexity - O(1)
        '''
        if not root:
            return True
        
        queue = [root, root]
        while queue:
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True
        '''


if __name__ == '__main-__':
    s = Solution()
    Tree = TreeNode(1)
    Tree.left = TreeNode(2)
    Tree.right = TreeNode(2)
    Tree.left.left = TreeNode(3)
    Tree.left.right = TreeNode(4)
    Tree.right.left = TreeNode(4)
    Tree.right.right = TreeNode(3)
    print(s.isSymmetric(Tree))