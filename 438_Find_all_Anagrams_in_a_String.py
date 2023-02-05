from itertools import permutations
class Solution:
    def findAnagrams(self, s: str, p: str):
        #Approach 1: Brute Force - Time Complexity: O(N^2) and Space Complexity - O(1)
        '''
        anagrams = ["".join(i) for i in permutations(p)]
        res = []
        for i in anagrams:
            if i in s:
                res.append(s.find(i))
        res.sort()
        return res
        '''

        #Approach 2: Sliding Window - TIme Complxity: O(N) and Space Complexity - O(1)
        '''
        res = []
        for i in range(len(s)-len(p)+1):
            if sorted(s[i:i+len(p)]) == sorted(p):
                res.append(i)
        return res
        '''

        #Approach 3: Sliding Window Optimized - TIme Complxity: O(N) and Space Complexity - O(1)
        res = []
        p_count = [0]*26
        s_count = [0]*26
        for i in p:
            p_count[ord(i)-ord('a')] += 1
        for i in range(len(s)):
            s_count[ord(s[i])-ord('a')] += 1
            if i >= len(p):
                s_count[ord(s[i-len(p)])-ord('a')] -= 1
            if s_count == p_count:
                res.append(i-len(p)+1)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
    print(s.findAnagrams("abab", "ab"))