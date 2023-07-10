import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        
        Map<String, String> hash = new HashMap();
        hash.put("1", "w");
        hash.put("-1", "s");
        hash.put("10", "d");
        hash.put("-10", "a");
        
        ArrayList<String> list = new ArrayList();
        for(int i = 1; i < numLog.length; i++) {
            answer = String.valueOf(numLog[i] - numLog[i-1]);
            list.add(hash.get(answer));
        }
        return String.join("", list);
    }
}