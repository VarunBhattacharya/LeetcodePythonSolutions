'''
You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.
'''

from collections import Counter
class Solution:
    def minimumRounds(self, tasks) -> int:
        #Better Method - Mathematical Approach - Time Complexity - O(N) and Space Complexity - O(N)
        '''
        hashCnt = collections.Counter(tasks)
        rounds = 0
        for i in hashCnt.values():
            if i == 1:
                return -1
            rounds += (i+2)//3
        return rounds
        '''

        #Better Method - Time Complexity - O(N) and Space Complexity - O(N)
        hashCnt = Counter(tasks)
        if 1 in hashCnt.values(): 
            return -1
        rounds = 0
        for i in hashCnt.values():
            rounds += i//3 + bool(i%3)
        return rounds

if __name__ == "__main__":
    tasks = tasks = [2,2,3,3,2,4,4,4,4,4]
    print(Solution().minimumRounds(tasks))