class Solution {
    public int[] solution(int n, int k) {    
        int cnt = n / k;
        int i = 1;
        int[] answer = new int[cnt];
        
        while(i <= cnt) {
            answer[i-1] = k*i;
            i++;
        }

        return answer;
    }
}
