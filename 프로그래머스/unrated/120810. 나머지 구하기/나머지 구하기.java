class Solution {
    public int solution(int num1, int num2) {
        // num1을 num2로 나누어 몫이 나올때까지
        // num1-num2
        // 더 이상 몫이 나오지 않으면 num1을 num2로 나눈 나머지가 남음
        while(num1 >= num2) {
            num1 -= num2;
        }
        return num1;
    }
}