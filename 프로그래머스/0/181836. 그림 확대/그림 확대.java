import java.util.*;
class Solution {
    public List<String> solution(String[] picture, int k) {
        List<String> rtnList = new ArrayList<String>();
        
        for(String pic:picture) {
            String row = "";
            for(int i = 0; i < pic.length(); i++) {
                for(int j = 0; j < k ; j++)
                    row += String.valueOf(pic.charAt(i));
            }
            for(int i = 0; i < k ; i++)
                rtnList.add(row);    
        }
        
        return rtnList;
    }
}