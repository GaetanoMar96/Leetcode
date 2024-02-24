class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < nums.length; i++) {
            maxHeap.add(nums[i]);
        }

        int res = 0;
        while(k > 0) {
            res = maxHeap.poll();
            k--;
        }
        return res;
    }
}