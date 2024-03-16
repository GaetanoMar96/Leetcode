
class ProductArrayExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] res = new int[length];
        Arrays.fill(res, 1);
        int shift = 1;
        for(int i = 0; i < length; i++){
            res[i] *= shift;
            shift *= nums[i];
        }
        shift = 1;
        for(int i = length - 1; i >= 0; i--){
            res[i] *= shift;
            shift *= nums[i];
        }
        return res;
    }
}