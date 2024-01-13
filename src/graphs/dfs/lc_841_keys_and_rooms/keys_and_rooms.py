class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        adj = {}
        def dfs(node, visited):
            if node in visited:
                return
            visited.add(node)
            if node in adj:
                for neigh in adj[node]:
                    if neigh not in visited:
                        dfs(neigh, visited)
        for i, room in enumerate(rooms):
            adj[i] = room
        visited = set()
        
        dfs(0, visited)
        return len(visited) == len(rooms)