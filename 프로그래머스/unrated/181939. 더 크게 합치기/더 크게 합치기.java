class Solution {
    public int solution(int a, int b) {       
        int a_b = Integer.valueOf(String.format("%s%s", a, b));
        int b_a = Integer.valueOf(String.format("%s%s", b, a));

        return a_b >= b_a ? a_b : b_a;
    }
}