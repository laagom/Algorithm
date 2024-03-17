class Solution {
    public int solution(int n) {
        int answer = 0;
        
        int i = 1;
        boolean flag = true;
        while(flag) {
            if(n%i == 1) {
                return i;
            }            
            i++;
        }
        return answer;
    }
}