package lc_424_longest_repeating_character_replacement;
import java.util.*;
class Solution {
    public static int characterReplacement(String s, int k) {
        Map<Character, Integer> occ = new HashMap<>();
        int window = 0, res = 0;
        int l=0;
        for(int r = 0; r < s.length(); r++){
            char current = s.charAt(r);
            if (occ.containsKey(current)) {
                occ.put(current, occ.get(current) + 1);
            } else {
                occ.put(current, 1);
            }
            window = occ.values().stream().mapToInt(Integer::intValue).sum();
            if (window - Collections.max(occ.values()) <= k) {
                res = Math.max(res, window);
                continue;
            }

            while(window - Collections.max(occ.values()) > k) {
                occ.put(s.charAt(l), occ.get(s.charAt(l)) - 1);
                window = occ.values().stream().mapToInt(Integer::intValue).sum();
                l++;
            }
        }
        res = Math.max(res, window);
        return res;
    }


}