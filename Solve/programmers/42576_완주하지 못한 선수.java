import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> pMap = new HashMap<>();
        
        for (String p: participant) {
            pMap.put(p, pMap.getOrDefault(p, 0) + 1);
        }
        
        for (String c: completion) {
            pMap.put(c, pMap.get(c) - 1);
            if (pMap.get(c) == 0) {
                pMap.remove(c);
            }
        }
        
        return pMap.keySet().iterator().next();
    }
}