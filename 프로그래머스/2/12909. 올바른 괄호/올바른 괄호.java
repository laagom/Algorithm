class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int openCnt = 0;
        int closeCnt = 0;
        int balance = 0;

        if(s.charAt(0) == ')' || s.charAt(s.length()-1) == '(' ) {
            return false;           
        }
        
        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) == '(') {
                openCnt ++;
                balance ++;
            }else if(s.charAt(i) == ')'){
                closeCnt ++;
                balance --;
            }
            
            if(balance < 0) {
                return false;
            }
        }
        
        if(openCnt != closeCnt)
            return false;
        
        return answer;
    }
}