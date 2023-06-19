from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        #Approach 1: Time Complexity - O(No.ofNodes) and Space Complexity - O(MaxNo.ofNodesInALevel)
        if not root:
            return 0
        
        q = deque([(root, 1)])

        while q:
            node, depth = q.popleft()
            for child in node.children:
                q.append((child, depth+1))
        
        return depth

if __name__ == "__main__":
    s = Solution()
    root = Node(1)
    root.children = [Node(3), Node(2), Node(4)]
    root.children[0].children = [Node(5), Node(6)]
    print(s.maxDepth(root))