# mine:(bfs)
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ind = [0 for _ in range(numCourses)]
        dit = [[] for _ in range(numCourses)]
        able = []
        sorted_list = []
        for i in prerequisites:
            dit[i[1]].append(i[0])
            ind[i[0]] += 1
        able = [i for i,j in enumerate(ind) if j == 0]
        while able:
            tmp = able.pop(0)
            sorted_list.append(tmp)
            for i in dit[tmp]:
                ind[i] -= 1
                if ind[i] == 0:
                    able.append(i)
        return sorted_list if len(sorted_list) == numCourses else []
