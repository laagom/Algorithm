import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> solution(int[] num_list, int n) {
        List<Integer> intList = Arrays.stream(num_list).boxed().collect(Collectors.toList());
        return intList.subList(n-1, num_list.length);
    }
}