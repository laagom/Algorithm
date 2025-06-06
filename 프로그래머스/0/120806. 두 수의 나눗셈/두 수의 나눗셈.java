class Solution {
    public double solution(int num1, int num2) {
        double answer = 0;
    
        //System.out.println(num1/(double)num2);
        //System.out.println((num1/(double)num2)*1000);
        
        // Parameter 조건 : num1, num2는 > 0, <= 100
        // 나눈 값이 소수점으로 나오게 하려면 num1, num2 중 하나에 double로 형변환.
        double value = num1/(double)num2;
        answer = value*1000;
        
        // 소수점 버리기 : Math.floor()
        return Math.floor(answer);
    }
}