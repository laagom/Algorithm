import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.stream.Collectors;

class Solution {
    public String solution(String my_string, int[] indices) {
        
        // indices를 ArrayList로 변환 하는데 Arrays.asList()를 사용하게 되면
        // List<int[]> 형식으로 들어가기 때문에 stream으로 변경해 줘야함
        List<String>  list = new ArrayList<>();
        List<Integer> indx = Arrays.stream(indices)
                            .boxed()
                            .collect(Collectors.toList());
        
        for(int i = 0; i < my_string.length(); i++) {
            if(!indx.contains(i)) {
                list.add(String.valueOf(my_string.charAt(i)));
            }
        }
        return String.join("", list);
    }
}