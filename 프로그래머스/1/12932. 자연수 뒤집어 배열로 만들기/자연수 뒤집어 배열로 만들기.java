import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<Integer> solution(long n) {
        List<Integer> rtnList = new ArrayList<Integer>();
        
        String numberStr = String.valueOf(n);
        for(int i = String.valueOf(n).length()-1; i >= 0; i--)
            rtnList.add(Integer.valueOf(String.valueOf(numberStr.charAt(i))));
        return rtnList;
    }
}