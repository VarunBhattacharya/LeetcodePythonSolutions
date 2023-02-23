import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital):
        #Optimized Approach: Time Complexity: O(nlogn) and Space Complexity: O(n)
        capital = [[capital[i], profits[i]] for i in range(0, len(capital))]
        capital.sort()
        heap = []
        for i in range(0, k):
            while capital and capital[0][0] <= w:
                heapq.heappush(heap, -capital[0][1])
                capital.pop(0)
            if heap:
                w -= heapq.heappop(heap)
            else:
                break
        return w

if __name__ == "__main__":
    s = Solution()
    print(s.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))