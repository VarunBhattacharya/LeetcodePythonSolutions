from collections import Counter
class Solution:
    def topKFrequent(self, nums, k: int):
        #Naive Approach - Time Complexity - O(NlogN) and Space Complexity = O(N)
        '''
        hashCnt = {}
        for i in nums:
            if i in hashCnt:
                hashCnt[i] += 1
            else:
                hashCnt[i] = 1
        
        #for sorting
        hashCnt = dict(sorted(hashCnt.items(), key = lambda x: x[1], reverse = True))
        
        res = []
        for i in hashCnt:
            res.append(i)
        return res[:k]
        '''

        #Better Approach - Using Counter - Time Complexity - O(N) and Space Complexity = O(N)
        hashCnt = Counter(nums)
        return [i[0] for i in hashCnt.most_common(k)]

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(Solution().topKFrequent(nums, k))