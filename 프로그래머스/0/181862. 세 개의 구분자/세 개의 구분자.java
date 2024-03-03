import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public List<String> solution(String myStr) {
        // a, b, c 갑승ㄹ 모두 동일한 a로 변환
        List<String> rtnList = new ArrayList<String>();
        myStr = myStr.replace("a","a").replace("b","a").replace("c","a");
        
        // aa가 중복으로 들어가는 경우 a로 변환
        while(myStr.contains("aa"))
            myStr = myStr.replace("aa", "a");
        
        // a기준으로 잘라 배열에 할당
        // 단, 빈값은 제외
        rtnList = new ArrayList<String>(Arrays.asList(myStr.split("a")));
        rtnList.remove("");
        
        // 반환시 배열에 값이 없다면 "EMPTY" 반환
        return rtnList.size() != 0 ? rtnList : new ArrayList<String>(Arrays.asList("EMPTY"));
    }
}