from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        #Approach 1
        '''
        res = []
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                res.append(nums2[i])
                nums1.remove(nums2[i])
        return res
        '''

        #Approach 2 - Bitwise Operation
        dict1, dict2 = Counter(nums1), Counter(nums2)
        return list((dict1 & dict2).elements())

if __name__ == '__main__':
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))
    print(s.intersect([1, 2, 3, 4], [2, 2, 3, 4, 5, 6, 7, 8, 9, 10]))