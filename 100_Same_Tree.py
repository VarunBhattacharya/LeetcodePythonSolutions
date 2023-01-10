# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        #Recursion Approach
        if p == None and q == None:
            return True
        else:
            if p == None or q == None:
                return False
            else:
                if p.val == q.val:
                    return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
                else:
                    return False

if __name__ == '__main__':
    obj = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(obj.isSameTree(p,q))