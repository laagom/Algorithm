class Solution {
    public int solution(int a, int b) { 
        switch(getNumberType(a, b)) {
            case 0:
                return Math.abs(a-b);
            case 1:
                return 2*(a+b);
            case 2:
                return (int)(Math.pow(a, 2) + Math.pow(b, 2));
        }   
        return 0;
    }
    
    public int getNumberType(int a, int b) {
        int cnt = 0;
        if(a%2 != 0) cnt ++;
        if(b%2 != 0) cnt ++;
        return cnt;
    }
}