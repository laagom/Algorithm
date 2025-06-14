class Solution {
    public int solution(int n) {
        return getSumDivisor(n);
    }
    
    public int getSumDivisor(int num) {
        int rtnVal = 0;
        for(int i = 1; i <= num; i++)
            if(num%i == 0) rtnVal += i;
        return rtnVal;
    }
}