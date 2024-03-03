import java.util.*;

class Solution {
    public List<Integer> solution(String myString) {
        List<Integer> intList = new ArrayList<Integer>();
        List<String> rtnList = new ArrayList<String>(Arrays.asList(myString.split("x")));
        
        if(myString.endsWith("x"))
            rtnList.add("");
        for(String str:rtnList)
            intList.add(str.length());
        
        return intList;
    }
}