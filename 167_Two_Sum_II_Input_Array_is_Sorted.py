class Solution:
    def twoSum(self, numbers, target: int):
        #Naive Approach - Time Complexity - O(N) and Space Complexity - O(N)
        '''
        hashMap = {}
        for ind, val in enumerate(numbers):
            diff = target - val
            if diff in hashMap:
                return [hashMap[diff]+1, ind+1]
            hashMap[val] = ind
        return
        '''

        #Better Approach - Binary Search - Time Complexity - O(NlogN) and Space Complexity - O(1)
        start, end = 0, len(numbers)-1
        while start < end: 
            curSum = numbers[start] + numbers[end]
            if curSum > target:
                end -= 1
            elif curSum < target:
                start += 1
            else:
                return [start + 1, end + 1]
        return

if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print(Solution().twoSum(numbers, target))