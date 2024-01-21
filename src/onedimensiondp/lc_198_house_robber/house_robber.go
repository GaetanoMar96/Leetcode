func rob(nums []int) int {
    n := len(nums)
    memo := make([]int, n)
    for i := range(memo) {
        memo[i] = -1
    }
    return dp(0, n, nums, memo)
}

func dp(i int, n int, nums []int, memo []int) int {
    if i >= n {
        return 0
    }
    if memo[i] != -1 {
        return memo[i]
    }
    temp1 := dp(i+1, n, nums, memo)
    temp2 := nums[i] + dp(i+2, n, nums, memo)
    if temp1 > temp2 {
        memo[i] = temp1
    } else {
        memo[i] = temp2
    }
    return memo[i]
}   