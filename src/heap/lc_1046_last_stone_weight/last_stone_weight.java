import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    final PriorityQueue<Integer> pq = new PriorityQueue<>(
        Comparator.reverseOrder()
    ); //max heap
    public int lastStoneWeight(int[] stones) {
        for(int i = 0; i < stones.length; i++) {
            pq.offer(stones[i]);
        }
        while(pq.size() > 1){
            int y = pq.remove();
            int x = pq.remove();
            if (y > x) {
                y = y - x;
                pq.offer(y);
            }
        }
        return pq.size() == 1 ? pq.remove() : 0;
    }
}