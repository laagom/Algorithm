import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.stream.Collectors;
class Solution {
    public List<Integer> solution(int[] arr) {
        int count = 0;
        
        List<Integer> rtnList = new ArrayList<Integer>();
        List<Integer> intList 
            = Arrays.stream(arr)
                    .boxed()
                    .collect(Collectors.toList());
        count = Collections.frequency(intList, 2);
        
        if(count == 0) {
            rtnList = new ArrayList<Integer>(Arrays.asList(-1));
        } else if(count == 1) {
            System.out.println(intList.indexOf(2));
            System.out.println(intList.size());
            rtnList = new ArrayList<Integer>(Arrays.asList(2));
            /*
            if(intList.size() == 1)
                rtnList = new ArrayList<Integer>(Arrays.asList(2));
                */
        } else if(count >= 2) {
            rtnList = intList.subList(intList.indexOf(2), intList.lastIndexOf(2)+1);
        }
        return rtnList;
    }
}