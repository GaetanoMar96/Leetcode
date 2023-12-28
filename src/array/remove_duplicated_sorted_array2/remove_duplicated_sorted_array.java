class Solution {
    public int removeDuplicates(int[] nums) {
        int count=1;
        int ptr = 1;
        int last = nums.length;
        while(ptr < last) {
            if (nums[ptr] == nums[ptr-1] && count < 2) {
                count++;
                ptr++;
            } else if (nums[ptr] == nums[ptr-1] && count == 2) {
                for(int j = ptr; j < last-1; j++) {
                    nums[j] = nums[j+1];
                }
                last--;
            } else {
                ptr++;
                count=1;
            }
        }
        return last;
    }
}