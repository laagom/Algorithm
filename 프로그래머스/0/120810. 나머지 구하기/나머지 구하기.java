class Solution {
    public int solution(int num1, int num2) {
        int answer = -1;
        if(num2 != 0) answer = num1%num2; 
        return answer;
    }
}