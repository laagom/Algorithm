import java.util.Map;
import java.util.HashMap;
class Solution {
    public int solution(int n, String control) {
        String[] array = control.split("");
        
        Map<String, Integer> hash = new HashMap();
        hash.put("w", 1);
        hash.put("s", -1);
        hash.put("d", 10);
        hash.put("a", -10);
        
        for(String str:array) {
            n += hash.get(str);
        }
        
        return n;
    }
}