class Solution {
    public long solution(long n) {
        long i = 0;
        while(i < 500000000) {
            if(n/1.0 == Math.pow(i, 2)) {
                return (long)Math.pow(i+1, 2);
            }
            i++;
        }
        return -1;
    }
}