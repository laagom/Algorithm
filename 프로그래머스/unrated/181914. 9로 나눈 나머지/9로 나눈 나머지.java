class Solution {
    public static final int _DID_NUMBER_9 = 9;
    
    public int solution(String numbers) {
        // 음이 아닌 정수 123을 9로 나누면 나머지는 6
        // 각 자리수의 합 6을 9로 나누면 나머지는 6
        String[] list = numbers.split("");
        int sum = 0;
        
        // 각 자리수의 합
        for(String number:list) {
            sum += Integer.valueOf(number);
        }
        
        return sum%_DID_NUMBER_9;
    }
}