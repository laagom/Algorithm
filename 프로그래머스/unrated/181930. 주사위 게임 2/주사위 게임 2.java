class Solution {
    public int solution(int a, int b, int c) {
        int answer = 0;
        
        if(a!=b && b!=c && c!=a) {
            answer = a+b+c;
        }else if(a==b && b==c && c==a) {
            answer = (a+b+c)*(getPow(a, 2)+getPow(b, 2)+getPow(c, 2))*(getPow(a, 3)+getPow(b, 3)+getPow(c, 3));
        }else {
            answer = (a+b+c)*(getPow(a, 2)+getPow(b, 2)+getPow(c, 2));
        }
        
        return answer;
    }
    
    public int getPow(int number, int powNumber) {
        return (int)Math.pow(number, powNumber);
    }
}