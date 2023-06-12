from itertools import accumulate

class Solution:
    def largestAltitude(self, gain) -> int:
        #Approach 1: Prefix Sum - Time Complexity - O(N) Space Complexity - O(N)
        '''
        maxAlt = float("-inf")
        res = [0]
        for i in range(len(gain)):
            res.append(gain[i] + res[-1])
        return max(res)
        '''

        #Approach 2: Using for loop - Time Complexity - O(N) Space Complexity - O(1)
        '''
        maxAlt = float("-inf")
        currAlt = 0
        for i in range(len(gain)):
            currAlt += gain[i]
            maxAlt = max(maxAlt, currAlt)
        return max(0, maxAlt)
        '''

        #Approach 3: One Liner - Time Complexity - O(N) Space Complexity - O(1)
        return max(0, max(accumulate(gain)))

if __name__ == '__main__':
    gain = [-5,1,5,0,-7]
    print(Solution().largestAltitude(gain))