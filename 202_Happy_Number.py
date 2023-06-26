class Solution:
    def isHappy(self, n: int) -> bool:
        #Approach 1: Time Complexity - O(N) and Space Complexity - O(N)
        if n == 1:
            return True

        checkCycle = set()

        def splitVal(n):
            nList = [int(dig)**2 for dig in str(n)]
            return sum(nList)
        
        while n != 1:
            n = splitVal(n)
            if n == 1:
                return True
            if n in checkCycle:
                return False
            checkCycle.add(n)
        
        return False

if __name__ == "__main__":
    print(Solution().isHappy(19))