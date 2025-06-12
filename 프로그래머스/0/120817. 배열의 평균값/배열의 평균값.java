class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int length = numbers.length;
        
        // 합구하기
        for(int num : numbers) answer += num;
        
        // 평균 반환
        return answer/length;
    }
}