import collections

class Solution:
    def distinctNames(self, ideas) -> int:
        #Approach 1 - Brute Force - Time Complexity - O(N^2) and Space Complexity - O(N)
        '''
        res = set()
        for i in range(len(ideas)):
            for j in range(i+1, len(ideas)):
                ideaA, ideaB = ideas[i], ideas[j]
                newIdeaA = ideaB[0] + ideaA[1:]
                newIdeaB = ideaA[0] + ideaB[1:]
                if newIdeaA not in ideas and newIdeaB not in ideas:
                    res.add(newIdeaA + " " + newIdeaB)
        return len(res)*2
        '''

        #Approach 2 - Better Solution - Time Complexity - O(N.26^2) and Space Complexity - O(N)
        charWordMap = collections.defaultdict(set)
        for word in ideas:
            charWordMap[word[0]].add(word[1:])
        
        res = 0
        for char1 in charWordMap:
            for char2 in charWordMap:
                if char1 == char2:
                    continue
                intersect = 0
                for word in charWordMap[char1]:
                    if word in charWordMap[char2]:
                        intersect += 1
                distinct1 = len(charWordMap[char1]) - intersect
                distinct2 = len(charWordMap[char2]) - intersect
                res += distinct1 * distinct2
        return res

if __name__ == "__main__":
    ideas = ["coffee","donuts","time","toffee"]
    print(Solution().distinctNames(ideas))