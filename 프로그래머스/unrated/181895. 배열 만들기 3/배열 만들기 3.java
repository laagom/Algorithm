import java.util.List;
import java.util.ArrayList;
class Solution {
    public List<Integer> solution(int[] arr, int[][] intervals) {
        List<Integer> list = new ArrayList<Integer>();
        int start = 0;
        int end = 0;
        for(int i = 0; i < intervals.length; i++) {
            start = intervals[i][0];
            end = intervals[i][1];
            for(int j = start; j <= end; j++) list.add(arr[j]);
        }
        return list;
    }
}