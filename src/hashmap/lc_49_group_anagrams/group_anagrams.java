import java.util.*;
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();
        for(String st : strs) {
            char[] charArray = st.toCharArray();
            Arrays.sort(charArray);
            String sortedString = new String(charArray);
            map.computeIfAbsent(sortedString, key -> new ArrayList<>()).add(st);
        }
        for(Map.Entry<String, List<String>> entry : map.entrySet()) {
            res.add(entry.getValue());
        }
        return res;
    }
}