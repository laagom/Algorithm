import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public List<String> solution(String myString) {
        List<String> rtnList = new ArrayList<String>(Arrays.asList(myString.split("x")));
        
        // 빈값이 들어가는 경우 제외 처리
        while(rtnList.contains("")) 
            rtnList.remove("");
        
        // 정렬
        Collections.sort(rtnList);
        return rtnList;
    }
}