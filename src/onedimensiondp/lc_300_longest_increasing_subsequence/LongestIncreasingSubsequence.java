class LongestIncreasingSubsequence {
    public int lengthOfLIS(int[] nums) {
        int length = nums.length;
        int[] dp = new int[length];
      
        for(int i = length - 1; i >= 0; i--) {
            int curr = nums[i];
            dp[i] = 1;
            for(int j = i+1; j < length; j++) {
                if(nums[j] > curr) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
        int max = Integer.MIN_VALUE;
        for(int i = 0; i < length; i++) {
            max = Math.max(max, dp[i]);
        }
        
        return max;
    }
    
}