import java.util.List;
import java.util.Collections;
import java.util.stream.IntStream;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> solution(int start, int end_num) {
        List<Integer> list = IntStream.rangeClosed(end_num, start)
                                .boxed()
                                .collect(Collectors.toList());
        
        Collections.reverse(list);
        return list;
    }
}