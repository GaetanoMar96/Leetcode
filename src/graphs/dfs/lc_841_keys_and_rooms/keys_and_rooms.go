func canVisitAllRooms(rooms [][]int) bool {
    adj := make(map[int][]int)
    visited := make(map[int]bool)
    for i, room := range rooms {
        adj[i] = room
    }
    dfs(adj, 0, visited)
    return len(visited) == len(rooms)
}

func dfs(adj map[int][]int, node int, visited map[int]bool) {
    _, ispresent := visited[node]
    if ispresent {
        return
    }
    visited[node] = true
    _, isNode := adj[node]
    if isNode {
        rooms := adj[node]
        for _, neigh := range(rooms) {
            dfs(adj, neigh, visited)
        }
    }
}