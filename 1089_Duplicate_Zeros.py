class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        #Naive Approach - Time Complexity = O(N) and Space Complexity - O(N)
        '''
        arr2 = []
        for i in range(len(arr)):
            if arr[i] == 0:
                arr2.append(0)
                arr2.append(0)
            else:
                arr2.append(arr[i])
        for i in range(len(arr)):
            arr[i] = arr2[i]
        return arr
        '''

        #Naive Approach 2 - Time Complexity - O(N) and Space Complexity - O(N)
        '''
        oldLen = len(arr)
        start, end = 0, len(arr)
        while start < end:
            if arr[start] == 0:
                arr.insert(start+1,0)
                start += 1
            start += 1
        arr[:] = arr[:oldLen]
        return arr
        '''

        #Better Approach - Pop from List - Time Complexity - O(N) and Space Complexity - O(1)
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i+1,0)
                arr.pop()
                i += 1
            i += 1
        return arr

if __name__ == '__main__':
    s = Solution()
    print(s.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
