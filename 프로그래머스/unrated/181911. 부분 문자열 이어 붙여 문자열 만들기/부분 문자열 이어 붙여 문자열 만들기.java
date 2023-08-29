import java.util.List;
import java.util.ArrayList;

class Solution {
    public String solution(String[] my_strings, int[][] parts) {       
        List answer = new ArrayList();
        int s               = 0;
        int e               = 0;
           
        for(int i = 0; i < parts.length; i++) {
            s = parts[i][0];
            e = parts[i][1];          
            answer.add(my_strings[i].substring(s, e+1));
        }

        return String.join("", answer);
    }
}