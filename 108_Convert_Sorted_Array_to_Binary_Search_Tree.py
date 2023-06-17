# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        #Approach 1: Time Complexity - O(N) and Space Complexity - O(1)
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
    

if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    s = Solution()
    print(s.sortedArrayToBST(nums))