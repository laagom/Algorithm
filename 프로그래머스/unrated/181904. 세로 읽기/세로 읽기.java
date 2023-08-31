import java.util.*;
import java.util.stream.*;
class Solution {
    public String solution(String my_string, int m, int c) {
//         String answer = "";
//         List<String> list = new ArrayList();

//         for(int i = 0; i < my_string.length(); i++) {
//             if(i%m == c-1) {
//                 list.add(String.valueOf(my_string.charAt(i)));
//             }    
//         }        
//         return String.join("", list);
            return IntStream.range(0, my_string.length())
            .filter(i -> i % m == c - 1)
            .mapToObj(i -> String.valueOf(my_string.charAt(i)))
            .collect(Collectors.joining());
    }
}