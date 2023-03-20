class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        #Approach 1: Intuitive Method - Time Complexity - O(N) and Space Complexity - O(N)
        flowerbedMod = [0] + flowerbed + [0]

        for i in range(1, len(flowerbedMod)-1):
            if flowerbedMod[i-1] == 0 and flowerbedMod[i] == 0 and flowerbedMod[i+1] == 0:
                flowerbedMod[i] = 1
                n -= 1
        return n <= 0

        #Approach 2: Better Space Complexity - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        empty = 0 if flowerbed[0] else 1

        for i in flowerbed:
            if i:
                n -= int((empty-1) / 2)
                empty = 0
            else:
                empty += 1
        n -= (empty) // 2
        return n <= 0
        '''


if __name__ == '__main__':
    print(Solution().canPlaceFlowers([1,0,0,0,1],1))