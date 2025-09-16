import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        int n = nums.length;
        HashSet<Integer> pSet = new HashSet<>();

        for (int num: nums) {
            pSet.add(num);
        }

        return pSet.size() > n/2 ? n/2 : pSet.size();
    }
}