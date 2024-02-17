class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            Character ch = s.charAt(i);
            if(map.containsKey(ch)){
                map.put(ch, map.get(ch) + 1);
            } else {
                map.put(ch, 1);
            }
        }
        List<Map.Entry<Character, Integer>> list = new ArrayList<>(map.entrySet());
        //sort a map using comparator
        list.sort((o1, o2) -> 
            // Comparing values in reverse order
             o2.getValue().compareTo(o1.getValue())
        );
        Map<Character, Integer> sortedMap = new LinkedHashMap<>();
        for (Map.Entry<Character, Integer> entry : list) {
            sortedMap.put(entry.getKey(), entry.getValue());
        }
        StringBuilder res = new StringBuilder();
        for (Map.Entry<Character, Integer> entry : sortedMap.entrySet()) {
            for(int i = 0; i < entry.getValue(); i++) {
                res.append(entry.getKey());
            }
        }
        return res.toString();
    }
}