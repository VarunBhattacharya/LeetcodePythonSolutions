class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        #Naive Approach: Time Complexity - O(N) and Space Complexity - O(N)
        '''
        maxVal = max(candies)
        resMat = []
        for i in candies:
            if (i + extraCandies) >= maxVal:
                resMat.append(True)
            else:
                resMat.append(False)
        return resMat
        '''

        #One Liner: Time Complexity - O(N) and Space Complexity - O(N)
        return [i + extraCandies >= max(candies) for i in candies]

if __name__ == '__main__':
    candies = [2,3,5,1,3]
    extraCandies = 3
    print(Solution().kidsWithCandies(candies, extraCandies))