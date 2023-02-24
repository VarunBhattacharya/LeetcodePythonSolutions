import heapq

class Solution:
    def minimumDeviation(self, nums):
        #Approach 1: Efficient Approach - Time Complexity: O(nlogm * logn), Space Complexity: O(n)
        minHeap, heapMax = [], 0
        for n in nums:
            temp = n
            while n % 2 == 0:
                n = n // 2
            minHeap.append((n,max(temp,2*n)))
            heapMax = max(heapMax, n)

        res = float('inf')
        heapq.heapify(minHeap)

        while len(minHeap) == len(nums):
            n, nMax = heapq.heappop(minHeap)
            res = min(res, heapMax-n)
            
            if n < nMax:
                heapq.heappush(minHeap, (n*2,nMax))
                heapMax = max(heapMax, n*2)

        return res
    
if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().minimumDeviation(nums))