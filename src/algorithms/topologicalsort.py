from collections import deque

def topologicalSort(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    courses = []
    adj = {}
    indegree = {}
    for i in range(numCourses):
        adj[i] = []
        indegree[i] = 0
        
    for a,b in prerequisites:
        adj[b].append(a)
        indegree[a] += 1
        
    q = deque()
    for course in indegree:
        if indegree[course] == 0:
            q.append(course)
        
    while q:
        course = q.popleft()
        courses.append(course)

        for neigh in adj[course]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                q.append(neigh)

    return courses if len(courses) == numCourses else []