class Solution {
    public int solution(int[] numbers, int n) {
        int answer = 0;
        int i = 0;
        for(int num : numbers) {
            // 순차적으로 numbers의 요소를 더함
            answer += num;
            
            // 더한 요소의 합이 넘겨 받은 n보다 커지면 반환
            if(answer > n) {
                return answer;
            }
            i++;
        }
        return answer;
    }
}