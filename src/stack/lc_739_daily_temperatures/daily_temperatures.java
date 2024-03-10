import java.util.*;
class Solution {

    class Pair {
        int key;
        int idx;
        Pair(int key, int idx) {
            this.key = key;
            this.idx = idx;
        }

        public int getKey() {
            return this.key;
        }

        public int getIdx() {
            return this.idx;
        }
    }
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Pair> stack = new Stack<>();
        int[] res = new int[temperatures.length]; //init with all 0
        for(int i = 0; i < temperatures.length; i++) {
            int temperature = temperatures[i];
            if(stack.isEmpty()){
                stack.push(new Pair(temperature, i)); //add temp and index
                continue;
            }
            //check if current temp > temp at peek of stack
            while(!stack.isEmpty()){
                if (temperature <= stack.peek().getKey()) {
                    break;
                }
                //if temperature > previou one
                Pair pair = stack.pop();
                res[pair.getIdx()] = i - pair.getIdx(); //calculate num of days curr idx - prev idx
            }
            stack.push(new Pair(temperature, i));
        }
        return res;
    }
}