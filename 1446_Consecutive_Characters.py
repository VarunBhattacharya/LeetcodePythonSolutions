class Solution:
    def maxPower(self, s: str) -> int:
        #Approach 1: Sliding Window - Time Complexity - O(N) and Space Complexity - O(1)
        maxCnt = 0
        pnt1, pnt2 = 0, 0

        tempCnt = 0

        while pnt2 < len(s):
            if s[pnt2] == s[pnt1]:
                tempCnt += 1
                pnt2 += 1
            else:
                maxCnt = max(maxCnt, tempCnt)
                pnt1 = pnt2
                tempCnt = 0
        maxCnt = max(maxCnt, tempCnt)
        return maxCnt

if __name__ == "__main__":
    s = "leetcode"
    print(Solution().maxPower(s))