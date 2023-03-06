class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        #Naive Approach: Time Complexity - O(N^2) and Space Complexity - O(1)
        '''
        for i in range(1, arr[-1]+1):
            if i not in arr:
                k -= 1
            if k == 0:
                return i
        return arr[-1] + k
        '''

        #Approach 2: Binary Search - Time COmplexity - O(logN) and Space Complexity - O(1)
        start = 0
        end = len(arr)-1
        while start <= end:
            mid = start+(end-start)//2
            if arr[mid]-mid-1 < k:
                start = mid+1
            else:
                end = mid-1
        return start+k
    

if __name__ == "__main__":
    # arr = [2,3,4,7,11]
    arr = [1,2,3,4]
    # k = 5
    k = 2
    print(Solution().findKthPositive(arr, k))