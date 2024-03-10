import java.util.*;
class KthLargest {

    final PriorityQueue<Integer> pq = new PriorityQueue(); //min heap
    final int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        for(int i = 0; i < nums.length; i++) {
            pq.offer(nums[i]);
        }
        while (pq.size() > k) {
            pq.remove();
        }
    }
    
    public int add(int val) {
        pq.offer(val);
        if(this.k < pq.size())
            pq.remove();
        int v = pq.remove();
        pq.offer(v);
        return v;
    }
}