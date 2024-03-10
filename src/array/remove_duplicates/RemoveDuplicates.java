class RemoveDuplicates {
    public int removeDuplicates(int[] nums) {
        int ptr = 1;
        int last = nums.length;
        while(ptr < last) {
            if (nums[ptr] == nums[ptr-1]) {
                for(int j = ptr; j < last-1; j++) {
                    nums[j] = nums[j+1];
                }
                last--;
            } else {
                ptr++;
            }
        }
        return last;
    }
}