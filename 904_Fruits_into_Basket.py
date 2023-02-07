import collections

class Solution:
    def totalFruit(self, fruits) -> int:
        #Approach 1 - Brute Force Solution - Time Complexity: O(n^2) and Space Complexity: O(n)
        '''
        maxCnt = 0
        for i in range(len(fruits)):
            cnt = 0
            basket = set()
            for j in range(i, len(fruits)):
                if fruits[j] not in basket:
                    if len(basket) == 2:
                        break
                    basket.add(fruits[j])
                cnt += 1
            maxCnt = max(maxCnt, cnt)
        return maxCnt
        '''

        #Approach 2 - Sliding Window - Time Complexity: O(n) and Space Complexity: O(n)
        hashMap = collections.defaultdict(int)
        left, winTotal, resTotal = 0,0,0
        for right in range(len(fruits)):
            hashMap[fruits[right]] += 1
            winTotal += 1
            while len(hashMap) > 2: #shrink the window
                fruit = fruits[left]
                hashMap[fruit] -= 1
                winTotal -= 1
                
                if hashMap[fruit] == 0:
                    hashMap.pop(fruit)
                left += 1
            resTotal = max(resTotal, winTotal)
        return resTotal

if __name__ == '__main__':
    fruits = [1,2,1]
    print(Solution().totalFruit(fruits))