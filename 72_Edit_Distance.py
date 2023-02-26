class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #Approach 1 - 2D DP Bottom-up approach - Time Complexity - O(N^2) and Space Complexity - O(N)
        '''
        cache = [[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)]

        #initialize base case
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        #bottom-up DP approach
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]: #if both characters are same
                    cache[i][j] = cache[i+1][j+1]
                else: #delete operation, insert operation, replace operation
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])

        return cache[0][0]
        '''

        #Approach 2 - 1D DP Bottom-up approach - Time Complexity - O(N^2) and Space Complexity - O(N)
        cache = [float("inf")] * (len(word2)+1)

        #initialize base case
        for j in range(len(word2) + 1):
            cache[j] = j

        #bottom-up DP approach
        for i in range(len(word1)):

            prev = cache[0]
            cache[0] = i + 1

            for j in range(len(word2)):
                temp = cache[j+1]
                if word1[i] == word2[j]: #if both characters are same
                    cache[j+1] = prev
                else: #delete operation, insert operation, replace operation
                    cache[j+1] = 1 + min(cache[j], cache[j+1], prev)
                prev = temp

        return cache[len(word2)]

if __name__ == '__main__':
    s = Solution()
    print(s.minDistance("horse", "ros"))
    print(s.minDistance("intention", "execution"))