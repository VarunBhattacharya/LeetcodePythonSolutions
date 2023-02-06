'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
'''

class Solution:
    def shuffle(self, nums, n: int):
        #Approach 1 - Two Pointer Method - Time Complexity - O(N) and Space Complexity - O(N)
        '''
        res = []
        i = 0
        j = n
        for i in range(n):
            res.append(nums[i])
            res.append(nums[j])
            j += 1
        return res
        '''

        #Approach 2 - List Comprehension - Time Complexity - O(N) and Space Complexity - O(N)
        '''
        res = [nums[i] for i in range(n) for j in range(2)]
        res[1::2] = nums[n:]
        return res
        '''

        #Approach 3 - In-place - Time Complexity - O(N) and Space Complexity - O(1) - Not Working
        '''
        for i in range(n):
            nums.insert(2*i+1, nums.pop())
        # nums[-1], nums[1] = nums[1], nums[-1]
        return nums
        '''

    

if __name__ == "__main__":
    nums = [2,5,1,3,4,7]
    n = 3
    print(Solution().shuffle(nums, n))