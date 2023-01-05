class Solution:
    def groupAnagrams(self, strs):
        #Naive Approach - Time Complexity - O(N) and Space Complexity - O(N)
        grpVal = {}
        for i in range(len(strs)):
            x = ''.join(sorted(strs[i]))
            if x not in grpVal:
                grpVal[x] = [strs[i]]
            else:
                grpVal[x].append(strs[i])
        return grpVal.values()

if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))