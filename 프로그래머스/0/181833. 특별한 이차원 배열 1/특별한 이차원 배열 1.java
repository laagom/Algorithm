import java.util.*;
class Solution {
    public List<List> solution(int n) {
        List<List> outList = new ArrayList<List>();
        List<Integer> inList = null;
        
        for(int i = 0; i < n; i++) {
            inList = new ArrayList<Integer>();
            for(int j = 0; j < n; j++) {
                if(i == j) {
                    inList.add(1);
                }else {
                    inList.add(0);
                }
            }
            outList.add(inList);     
        }
        return outList;
    }
}