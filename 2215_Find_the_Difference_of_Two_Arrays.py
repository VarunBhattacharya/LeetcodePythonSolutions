class Solution:
    def findDifference(self, nums1, nums2):
        #Approach 1: Time Complexity - O(N) and Space Complexity - O(N)
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]
    
        #Approach 2: Time Complexity - O(N) and Space Complexity - O(N)
        '''
        res = []
        temp = []
        
        for i in nums1:
            if i not in nums2 and i not in temp:
                temp.append(i)
        res.append(temp)
            
        temp = []
        for i in nums2:
            if i not in nums1 and i not in temp:
                temp.append(i)
        res.append(temp)
        
        return res
        '''

if __name__ == '__main__':
    nums1 = [1,2,3,]
    nums2 = [2,4,6]
    print(Solution().findDifference(nums1, nums2))