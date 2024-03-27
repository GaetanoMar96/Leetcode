class FirstMissingPositive {
    public int firstMissingPositive(int[] nums) {
        Arrays.sort(nums);

        if (nums[0] > 1) {
            return 1;
        }
        if (nums[nums.length - 1] <= 0) {
            return 1;
        }

        int currmin = 0;
        boolean diff = false;
        int temp = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] > 0) {
                temp = i;
                break;
            }
        }
        if (nums[temp] > 1) {
            return 1;
        }
        for (int i = temp; i < nums.length-1; i++) {
            if (nums[i+1] - nums[i] > 1) {
                currmin = nums[i] + 1;
                diff = true;
                break;
            }
        }

        // If no positive missing integer found, return the next positive integer
        if (!diff) {
            return nums[nums.length - 1] + 1;
        } 
        return currmin;
    }
}