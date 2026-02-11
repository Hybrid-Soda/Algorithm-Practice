import java.util.HashSet;

class 폰켓몬_1845 {
    public int solution(int[] nums) {
        int n = nums.length;
        HashSet<Integer> pSet = new HashSet<>();

        for (int num: nums) {
            pSet.add(num);
        }

        return pSet.size() > n/2 ? n/2 : pSet.size();
    }
}