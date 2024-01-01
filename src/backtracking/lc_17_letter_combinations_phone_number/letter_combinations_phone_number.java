class Solution {

    static Map<Character, List<Character>> map = new HashMap<>();
    List<String> res = new ArrayList<>();

    static {
        map.put('2', Arrays.asList('a', 'b', 'c'));
        map.put('3', Arrays.asList('d', 'e', 'f'));
        map.put('4', Arrays.asList('g', 'h', 'i'));
        map.put('5', Arrays.asList('j', 'k', 'l'));
        map.put('6', Arrays.asList('m', 'n', 'o'));
        map.put('7', Arrays.asList('p', 'q', 'r', 's'));
        map.put('8', Arrays.asList('t', 'u', 'v'));
        map.put('9', Arrays.asList('w', 'x', 'y', 'z'));
    }

    public List<String> letterCombinations(String digits) {
        if (digits.equals("")) {
            return res;
        }
        backtrack(0, digits, new ArrayList<>());
        return res;
    }

    public void backtrack(int i, String digits, List<Character> comb) {
        if(comb.size() == digits.length()) {
            res.add(comb.stream()
            .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
            .toString());
            return;
        }
        for (int j = i; j < digits.length(); j++) {
            for(Character ch : map.get(digits.charAt(j))){
                comb.add(ch);
                backtrack(j+1, digits, comb);
                comb.remove(comb.size()-1);
            }
        }
    }
}