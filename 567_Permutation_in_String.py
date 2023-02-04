from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Approach - 1 - Naive Method
        '''
        allPermut = [''.join(i) for i in permutations(s1)]
        for i in allPermut:
            if i in s2:
                return True
        return False
        '''

        #Approach - 2 - Sliding Window using HashMap - TC - O(N) and SC - O(N)
        if len(s1) > len(s2):
            return False
        s1Count, s2Count = [0]*26, [0]*26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        #sliding window
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            ind = ord(s2[right]) - ord('a')
            s2Count[ind] += 1
            if s1Count[ind] == s2Count[ind]:
                matches += 1
            elif s1Count[ind]+1 == s2Count[ind]:
                matches -= 1
            
            ind = ord(s2[left]) - ord('a')
            s2Count[ind] -= 1
            if s1Count[ind] == s2Count[ind]:
                matches += 1
            elif s1Count[ind]-1 == s2Count[ind]:
                matches -= 1
            left += 1
        return matches == 26
        
    
if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(Solution().checkInclusion(s1, s2))