import java.util.*;
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i = 0; i < nums2.length; i++) {
            pq.add(nums2[i]);
        }

        int ptr = 0;
        while(ptr < m) {
            if(!pq.isEmpty() && nums1[ptr] > pq.peek()) {
                int ele = pq.poll();
                int temp = nums1[ptr];
                nums1[ptr] = ele;
                pq.add(temp);
            }
            ptr++;
        }
        int i = m;
        while(!pq.isEmpty()) {
            nums1[i] = pq.poll();
            i++;
        }
    }
}
