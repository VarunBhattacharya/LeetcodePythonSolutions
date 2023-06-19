from collections import Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root):
        #Approach 1: Time Complexity - O(Height) and Space Complexity - O(1)
        res = []
        def inorder(root):
            if not root:
                return
            else:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        
        inorder(root)

        c = Counter(res)
        return [num for num, cnt in c.items() if cnt == max(c.values())]

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)

    obj = Solution()
    print(obj.findMode(root))