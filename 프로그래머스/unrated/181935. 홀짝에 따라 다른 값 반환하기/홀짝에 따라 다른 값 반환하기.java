class Solution {
    public int solution(int n) {
        return n%2 == 0 ? oven_sum(n) : odd_sum(n);
    }
    
    public int odd_sum(int n){
        // 홀수인 경우 계산식
        int count = 0;
        for(int i = 1; i <= n; i++){
            if(i%2 == 1){
               count += i; 
            }
        }
        return count;
    }
    
    public int oven_sum(int n){
        // 짝수인 경우 계산식
        int count = 0;
        for(int i = 1; i <= n; i++){
            if(i%2 == 0){
               count += Math.pow(i, 2); 
            }
        };
        return count;
    }
}