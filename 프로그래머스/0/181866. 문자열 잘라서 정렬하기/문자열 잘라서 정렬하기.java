import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public List<String> solution(String myString) {
        List<String> rtnList = new ArrayList<String>(Arrays.asList(myString.split("x")));
        
        while(rtnList.contains("")) {
            rtnList.remove("");
        }
        Collections.sort(rtnList);
        return rtnList;
    }
}