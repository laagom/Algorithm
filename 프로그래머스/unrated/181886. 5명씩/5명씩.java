import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<String> solution(String[] names) {
        List<String> list = new ArrayList<String>();
        final int groupCnt = 5;
        
        int i = 0;
        for(String name : names) {
            if(i%groupCnt == 0) {
                list.add(name);
            }
            i++;
        }
        
        return list;
    }
}