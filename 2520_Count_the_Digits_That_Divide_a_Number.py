class Solution:
    def countDigits(self, num: int) -> int:
        #Naive Approach - Time Complexity - O(N) and Space Complexity - O(N)
        '''
        digPresent = [int(x) for x in str(num)]
        cnt = 0
        for i in range(len(digPresent)):
            if num % digPresent[i] == 0:
                cnt += 1
        return cnt
        '''

        #Better Memory Approach - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        strNum = str(num)
        cnt = 0
        for i in strNum:
            if num % int(i) == 0:
                cnt += 1
        return cnt
        '''

        #One Liner Approach - Time Complexity - O(N) and Space Complexity - O(1)
        return sum(1 if num%int(i) == 0 else 0 for i in str(num))

if __name__ == '__main__':
    obj = Solution()
    print(obj.countDigits(121))