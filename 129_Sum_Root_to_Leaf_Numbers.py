# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root) -> int:
        #Approach 1: Recursion - Time Complexity - O(height) and Space Complexity - O(1)
        def sumRootToLeafVals(root, res):
            if root is None:
                return 0
            res = res*10 + root.val

            if root.left is None and root.right is None:
                return res
            
            return (sumRootToLeafVals(root.left, res) + sumRootToLeafVals(root.right, res))

        return sumRootToLeafVals(root, 0)
    

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(s.sumNumbers(root))