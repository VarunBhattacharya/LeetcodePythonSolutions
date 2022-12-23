class Solution:
    def mySqrt(self, x: int) -> int:
        #Naive Solution
        '''
        return int(pow(x,0.5))
        '''

        #Better Solution - Binary Search - O(logN) solution
        '''
        left, right, mid = 0, x, 0
        while left <= right:
            mid = (left+right)//2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid

        return right
        '''

        #Better Solution - Newton Rhapson Method - O(logN) solution
        res = x
        while not res * res - x < 1:
            res = (res + x / res)/2
        return int(res)

if __name__ == '__main__':
    x = 8
    print(Solution().mySqrt(x))