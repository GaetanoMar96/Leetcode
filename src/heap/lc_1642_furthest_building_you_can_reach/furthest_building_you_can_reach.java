import java.util.*;
class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(
            (a, b) -> b - a//add comparator
        );
        int diff;
        for(int i = 0; i < heights.length - 1; i++) {
            diff = heights[i+1] - heights[i];
            if(diff <= 0) //no need to use ladder or bricks
                continue;
            
            bricks -= diff;
            pq.offer(diff);
            if (bricks < 0) {
                if (ladders == 0)
                    return i;
                ladders--;
                int recover = pq.poll();
                bricks += recover;
            }
        }
        return heights.length - 1;
    }
}