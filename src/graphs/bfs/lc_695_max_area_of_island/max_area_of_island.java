class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int area = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    area = Math.max(area, bfs(grid, i, j));
                }
            }
        }

        return area;
    }

    private int bfs(int[][] grid, int i, int j) {
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{i, j});

        int[][] directions = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        int area = 1;
        grid[i][j] = 2;

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int r = current[0];
            int c = current[1];

            for (int[] direction : directions) {
                int rx = r + direction[0];
                int cy = c + direction[1];

                if (0 <= rx && rx < grid.length && 0 <= cy && cy < grid[0].length && grid[rx][cy] == 1) {
                    q.offer(new int[]{rx, cy});
                    grid[rx][cy] = 2;
                    area += 1;
                }
            }
        }

        return area;
    }
}