import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> solution(int[] arr, int[] query) {
        List<Integer> intList = getList(arr);
        
        for(int i = 0; i < query.length; i++) {
            //System.out.println(i +"이전"+ intList);
            // 짝수인 경우
            if(i%2 == 0) {
                intList = intList.subList(0, query[i]+1);
            } else {
                // 홀수인 경우
                intList = intList.subList(query[i], intList.size());
            }
            //System.out.println(i +"이후"+ intList);
        }
        //System.out.println(intList);
        return intList;
    }
    public List<Integer> getList(int [] intList) {
        List<Integer> list = new ArrayList<Integer>();
        for(int i=0; i < intList.length; i++) {
            list.add(intList[i]);
        }
        return list;
    }
}

