from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # must take b before a
        if prerequisites == []:
            return True
        adj = defaultdict(list)
        indegree = {}
        q = deque()
        # init indegree
        for i in range(numCourses):
            indegree[i] = 0
        for p in prerequisites:
           a, b = p
           adj[b].append(a)
           #check direction of arrow b -> a, a has an indegree
           indegree[a] += 1

        for k in indegree:
            if indegree[k] == 0:
                #define starting point
                q.append(k)
                
        # start bfs
        prereq = 0
        while q:
            node = q.popleft()
            prereq += 1
            for neigh in adj[node]:
                if neigh in indegree:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        q.append(neigh)
        return prereq == numCourses

