class Solution {

    Map<Integer, Integer> map = new HashMap<>();

    public int climbStairs(int n) {
        return dp(0, n);
    }

    public int dp(int steps, int n) {
        if (map.containsKey(steps))
            return map.get(steps);
        if (steps > n)
            return 0;
        if (steps == n)
            return 1;
        int ans = dp(steps + 1, n) + dp(steps + 2, n);
        map.put(steps, ans);
        return ans;
    }
}