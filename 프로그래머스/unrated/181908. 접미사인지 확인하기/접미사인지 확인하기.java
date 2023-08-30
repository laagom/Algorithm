import java.util.List;
import java.util.ArrayList;

class Solution {
    public int solution(String my_string, String is_suffix) {
        int answer = 0;
        List<String> list = new ArrayList<String>();
        
        for(int i = 0; i < my_string.length(); i++) {
            list.add(my_string.substring(i, my_string.length()));
        }

        return list.contains(is_suffix) == true ? 1 : 0;
    }
}