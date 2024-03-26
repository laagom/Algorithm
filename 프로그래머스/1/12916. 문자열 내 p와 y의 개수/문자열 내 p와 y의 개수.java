class Solution {
    boolean solution(String s) {
        // p & y가 하나도 포함되지 않은경우
        s = s.toLowerCase();
        if(!s.contains("p") && !s.contains("y")) {
            return true;
        }
        
        // p & y의 각각의 포함 개수
        long pCnt = s.chars().filter(c -> c == 'p').count();
        long yCnt = s.chars().filter(c -> c == 'y').count();
    
        return pCnt == yCnt ? true : false;
    }
}