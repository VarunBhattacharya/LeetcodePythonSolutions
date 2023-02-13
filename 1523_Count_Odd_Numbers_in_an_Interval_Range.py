class Solution:
    def countOdds(self, low: int, high: int) -> int:
        #Approach 1: Naive Approach - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        cnt = 0
        for i in range(low, high+1):
            if i%2 != 0: cnt += 1
        return cnt
        '''

        #Approach 2: Better Method - Time Complexity - O(1) ans Space Complexity - O(1)
        if low%2==0 and high%2==0:
            return (high-low)//2
        else:
            return ((high-low)//2)+1

if __name__ == "__main__":
    obj = Solution()
    print(obj.countOdds(3,7))