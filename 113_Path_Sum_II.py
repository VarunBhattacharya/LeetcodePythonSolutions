# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum: int):
        #Approach 1: DFS - Time Complexity - O(Nodes * Height) and Space Complexity - O(Height)
        '''
        totPaths = []

        def dfs(node, currSum, path):
            if not node:
                return []
            currSum += node.val
            path.append(node.val)
            if not node.left and not node.right:
                if currSum == targetSum:
                    totPaths.append(path[:])
            leftPath = dfs(node.left, currSum, path)
            rightPath = dfs(node.right, currSum, path)
            path.pop()
            return leftPath + rightPath
        
        dfs(root, 0, [])
        return totPaths
        '''

        #Approach 2: BFS - Time Complexity - O(Nodes * Height) and Space Complexity - O(Height)
        if not root:
            return []
        totPaths = []
        queue = [(root, root.val, [root.val])]
        while queue:
            node, currSum, path = queue.pop(0)
            if not node.left and not node.right and currSum == targetSum:
                totPaths.append(path)
            if node.left:
                queue.append((node.left, currSum + node.left.val, path + [node.left.val]))
            if node.right:
                queue.append((node.right, currSum + node.right.val, path + [node.right.val]))
        return totPaths
    

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    # root.right.right.left = TreeNode(5)
    # root.right.right.right = TreeNode(1)
    targetSum = 22
    print(Solution().pathSum(root, targetSum))