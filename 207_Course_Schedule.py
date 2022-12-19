class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        #initializing the hashMap
        preMap = {i:[] for i in range(numCourses)}

        #add the values in the hashMap
        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        #initializing the set which contains the visited nodes
        visitSet = set()

        #use dfs for finding the preq courses recursively
        def dfs(crs):
            if crs in visitSet: #check for a loop in the graph
                return False
            if preMap[crs] == []: #if no preq exist
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): #if it has preq
                    return False
            
            visitSet.remove(crs) #if the course has completed visiting
            preMap[crs] = [] #to confirm that this course can be taken
            return True
        
        #run for all the courses given
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1,0]]
    print(Solution().canFinish(numCourses, prerequisites))