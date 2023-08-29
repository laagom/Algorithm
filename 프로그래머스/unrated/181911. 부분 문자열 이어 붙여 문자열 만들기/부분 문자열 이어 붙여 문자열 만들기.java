//------------------------------- [내 풀이 방법] ------------------------------- //
// import java.util.List;
// import java.util.ArrayList;

// class Solution {
//     public String solution(String[] my_strings, int[][] parts) {       
//         List answer = new ArrayList();
//         int s               = 0;
//         int e               = 0;
           
//         for(int i = 0; i < parts.length; i++) {
//             s = parts[i][0];
//             e = parts[i][1];          
//             answer.add(my_strings[i].substring(s, e+1));
//         }
// 
//         return String.join("", answer);
//     }
// }

// ------------------------------- [Stream을 이용한 풀이 방법] ------------------------------- //
import java.util.stream.*;

class Solution {
    public String solution(String[] myStrings, int[][] parts) {
        
        return IntStream.range(0, myStrings.length).mapToObj(i -> myStrings[i].substring(parts[i][0], parts[i][1] + 1)).collect(Collectors.joining());
    }
}