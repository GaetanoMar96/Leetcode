import java.util.*;
class Solution {
    Map<Integer, Integer> map = new HashMap<>();

    public int minCostClimbingStairs(int[] cost) {
        return Math.min(dp(cost, 0), dp(cost, 1));
    }

    public int dp(int[] cost, int i) {
        if (map.containsKey(i))
            return map.get(i);
        if(i >= cost.length)
            return 0;
        int res = cost[i];
        res += Math.min(dp(cost, i+1), dp(cost, i+2));
        map.put(i, res);
        return res;
    }
}