class Solution {
    public int solution(int[] num_list) {
        int powOfSum = 0;
        int mul = 1;
        
        for(int num:num_list) {
            mul *= num;
            powOfSum += num;
        }

        return mul < (int)Math.pow(powOfSum, 2) ? 1 : 0;
    }
}