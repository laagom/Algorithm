class Solution {
    public int solution(int n) {
        int answer = 0;
        // n보다 작은수 중에서 2로 나눴을때 나머지가 0인 경우
        for(int i = 0; i <= n; i++)
            if(i%2 == 0) answer += i;
        return answer;
    }
}