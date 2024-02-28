import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public List<String> solution(String[] strArr) {
        String keyword = "ad";
        List<String> strArrList = new ArrayList<>(Arrays.asList(strArr));
        for(int i = 0; i < strArr.length; i++ ) {
            if(strArr[i].contains(keyword))
                strArrList.remove(strArr[i]);
        }
        return strArrList;
    }
}