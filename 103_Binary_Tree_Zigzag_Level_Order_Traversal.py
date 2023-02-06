# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        #Approach 1 - BFS Algorithm - Time COmplexity - O(2*height) and Space Complexity - O(N)
        '''
        if not root:
            return
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
        return [res[i][::-1] if i%2==1 else res[i] for i in range(len(res))]
        '''

        #Approach 2 - DFS Algorithm - Time Complexity - O(2*height) and Space Complexity - O(N)
        if not root:
            return
        res = []
        def dfs(root, level):
            if not root:
                return
            if len(res) == level:
                res.append([])
            if level%2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        return res

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().zigzagLevelOrder(root))    