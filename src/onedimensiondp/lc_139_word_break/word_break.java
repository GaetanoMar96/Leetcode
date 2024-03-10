import java.util.*;

class Solution {

    Set<String> wordSet;
    Map<String, Boolean> memo = new HashMap<>();

    public boolean wordBreak(String s, List<String> wordDict) {
        wordSet = new HashSet<>(wordDict);
        return dp(s, "");
    }

    public boolean dp(String s, String build) {
        if (memo.containsKey(s))
            return memo.get(s);
        if (wordSet.contains(s) || s.equals(""))
            return true;
        for(int i = 0; i < s.length(); i++){
            build = build + s.charAt(i);
            if (wordSet.contains(build)) {
                memo.put(s, dp(s.substring(i+1), ""));
                if (memo.get(s))
                    return true;
            }
        }
        return false;
    }
}