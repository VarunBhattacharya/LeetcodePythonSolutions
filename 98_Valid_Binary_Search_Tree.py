# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        #Approach 1: Time Complexity - O(Height) and Space Complexity - O(1)
        def checkValidBST(root, left, right):
            if not root:
                return True
            if not (root.val < right and root.val > left):
                return False
            return (checkValidBST(root.right, root.val, right) and 
                    checkValidBST(root.left, left, root.val))
        
        return checkValidBST(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(Solution().isValidBST(root))