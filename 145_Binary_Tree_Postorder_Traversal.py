# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root):
        #Recursive Approach
        res = []
        def postOrder(root):
            if not root:
                return
            else:
                postOrder(root.left)
                postOrder(root.right)
                res.append(root.val)
        postOrder(root)
        return res

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().postorderTraversal(root))