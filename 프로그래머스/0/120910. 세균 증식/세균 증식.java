class Solution {
    public int solution(int n, int t) {
        int expandCnt = n;
        for(int i = 0; i < t; i++) expandCnt = expandCnt*2;
        return expandCnt;
    }
}