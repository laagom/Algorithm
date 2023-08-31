import java.util.List;
import java.util.ArrayList;
import java.util.stream.*;

class Solution {
    public String solution(int q, int r, String code) {
        List list = new ArrayList<>();
        for(int i = 0; i < code.length(); i++) {
            if(i%q == r) {
                list.add(String.valueOf(code.charAt(i)));
            }
        }
        return String.join("", list);
        // return IntStream.range(0, code.length())
        //     .filter(i -> i%q == r)
        //     .mapToObj(i -> String.valueOf(code.charAt(i)))
        //     .collect(Collectors.joining());
    }
}