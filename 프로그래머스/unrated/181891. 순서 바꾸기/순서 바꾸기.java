import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;
class Solution {
    public List<Integer> solution(int[] num_list, int n) {
        int stdNum = n;
        List<Integer> bTrimList = new ArrayList<Integer>();
        List<Integer> aTrimList = new ArrayList<Integer>();
        List<Integer> intList 
            = Arrays.stream(num_list)
                    .boxed()
                    .collect(Collectors.toList());
    
        bTrimList = intList.subList(stdNum, num_list.length);
        aTrimList = intList.subList(0, stdNum);
        bTrimList.addAll(aTrimList);
        
        return bTrimList;
    }
}