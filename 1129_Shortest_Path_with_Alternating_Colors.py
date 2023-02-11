import collections

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges, blueEdges):
        #Approach 1: BFS - Time Complexity - O(N) and Space Complexity - O(N)
        redMap = collections.defaultdict(list)
        blueMap = collections.defaultdict(list)

        for src, dst in redEdges:
            redMap[src].append(dst)

        for src, dst in blueEdges:
            blueMap[src].append(dst)

        answer = [-1 for _ in range(n)]

        queue = collections.deque()
        queue.append([0,0,None]) #node, length, prev_edge_color
        visitSet = set() #visited node hashset
        visitSet.add((0,None))

        while queue: #bfs approach
            currNode, nodeLength, prevEdgeColor = queue.popleft()
            
            if answer[currNode] == -1:
                answer[currNode] = nodeLength
            
            if prevEdgeColor != "RED":
                for neighbour in redMap[currNode]:
                    if (neighbour, "RED") not in visitSet:
                        visitSet.add((neighbour, "RED"))
                        queue.append([neighbour, nodeLength+1, "RED"])
            
            if prevEdgeColor != "BLUE":
                for neighbour in blueMap[currNode]:
                    if (neighbour, "BLUE") not in visitSet:
                        visitSet.add((neighbour, "BLUE"))
                        queue.append([neighbour, nodeLength+1, "BLUE"])
        return answer

if __name__ == "__main__":
    n = 3
    redEdges = [[0,1],[1,2]]
    blueEdges = []
    print(Solution().shortestAlternatingPaths(n, redEdges, blueEdges))