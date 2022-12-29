class Solution:
    def haveConflict(self, event1, event2) -> bool:
        return max(event1[0], event2[0]) <= min(event1[1], event2[1])

if __name__ == '__main__':
    s = Solution()
    print(s.haveConflict([1, 2], [2, 3]))