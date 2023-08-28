class Solution {
    public String solution(String my_string, int[][] queries) {
        StringBuffer sb = null;
        String var1     = null;
        String pre      = null;
        String mid      = null;
        String fix      = null;
        int s = 0;
        int e = 0;
        
        for(int[] query:queries) {
            s   = query[0];
            e   = query[1];
            
            // StringBuffer - reverse() 함수 이용
            sb  = new StringBuffer(my_string.substring(s, e+1));
            
            pre = my_string.substring(0, s);
            mid = String.valueOf(sb.reverse());
            fix = my_string.substring(e+1, my_string.length());
            
            // substring 앞부분 + 뒤집는 부분 + 뒷부분
            my_string = pre + mid + fix;
        }     
        return my_string;
    }
}