import java.util.*;
class Solution {

    Map<Integer, List<Integer>> adj = new HashMap<>();

    Map<Integer, Integer> indegree = new HashMap<>();
    
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        for (int i = 0; i < numCourses; i++){
            indegree.put(i, 0);
        }
        for (int[] prerequisite : prerequisites) {
            int a = prerequisite[0];
            int b = prerequisite[1];
            adj.computeIfAbsent(b, key -> new ArrayList<>()).add(a);
            indegree.put(a, indegree.get(a) + 1);
        }
        Deque<Integer> q = new ArrayDeque<>();
        for(int key : indegree.keySet()) {
            if (indegree.get(key) == 0) {
                q.addLast(key);
            }
        }
        return getTotalCourses(q) == numCourses;
    }

    public int getTotalCourses(Deque<Integer> q) {
        int courses = 0;
        while (!q.isEmpty()) {
            int node = q.removeFirst();
            courses += 1;
            if (adj.containsKey(node)) {
                for (Integer neigh : adj.get(node)) {
                    if (indegree.containsKey(neigh)) {
                        indegree.put(neigh, indegree.get(neigh) - 1);
                        if (indegree.get(neigh) == 0)
                            q.addLast(neigh);
                    }
                }
            }
        }
        return courses;
    }
}