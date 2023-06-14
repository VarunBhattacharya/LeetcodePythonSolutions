from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        #Approach 1: Time Complexity - O(N) and Space Complexity - O(1)
        countObj = Counter(arr)
        return len(set(countObj.values())) == len(countObj.values())


if __name__ == '__main__':
    arr = [1,2,2,1,1,3]
    print(Solution().uniqueOccurrences(arr))