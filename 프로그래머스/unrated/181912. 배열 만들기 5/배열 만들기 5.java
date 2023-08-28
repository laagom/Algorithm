import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<Integer> solution(String[] intStrs, int k, int s, int l) {
        List<Integer> answer = new ArrayList<Integer>();
        
        for(String str:intStrs) {
            int number = Integer.valueOf(str.substring(s, s+l));
            if(number > Integer.valueOf(k)) {
                answer.add(number);
            }
        }
        return answer;
    }
}