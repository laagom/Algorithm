class Solution {
    public int solution(int n) {
        return getDiviSor(n);
    }
    
    public int getDiviSor(int n) {
        int amount = 0;
        for(int i = 1; i <= n; i++) {
            if(n%i == 0)
                amount += i;
        }
        return amount;
    }
}