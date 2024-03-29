# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #Approach 1: Binary Search - Time Complexity - O(logN) and Space Complexity - O(1)
        start = 0
        end = n

        while start <= end:
            mid = start + (end - start) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                end = mid - 1
            else:
                start = mid + 1
        
        return 0
    
if __name__ == "__main__":
    s = Solution()
    print(s.guessNumber(10))