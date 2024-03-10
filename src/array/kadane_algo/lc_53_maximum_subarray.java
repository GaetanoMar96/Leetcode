import java.util.*;
class Solution {
    public int maxSubArray(int[] nums) {
        int max = Arrays.stream(nums).max().getAsInt();
        if (max < 0) {
            return max;
        }
        return maximumSubarray(nums);
    }

    public int maximumSubarray(int[] nums) {
        int currsum = 0;
        int maxsum = Integer.MIN_VALUE;
        for(int i = 0; i < nums.length; i++) {
            if (currsum + nums[i] < 0) {
                currsum = 0;
                continue;
            }
            currsum = currsum + nums[i];
            maxsum = Math.max(maxsum, currsum);
        }
        return maxsum;
    }
}