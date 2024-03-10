import java.util.*;
class RandomizedSet {

    Set<Integer> keys;
    Random random;
    public RandomizedSet() {
        keys = new HashSet<>();
        random = new Random();
    }
    
    public boolean insert(int val) {
        if(keys.contains(val)) {
            return false;
        }
        keys.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if(keys.contains(val)) {
            keys.remove(val);
            return true;
        }
        return false;
    }
    
    public int getRandom() {
        int randomIndex = random.nextInt(keys.size());
        List<Integer> keyslist = new ArrayList<>(keys);
        return keyslist.get(randomIndex);
    }
}

