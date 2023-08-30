// import java.util.List;
// import java.util.ArrayList;
// import java.util.Comparator;

// class Solution {
//     public List<String> solution(String my_string) {
//         List<String> list = new ArrayList<>();
        
//         // "banana"의 b 인덱스 1부터 시작하여 a 마지막 인덱스 까지 순회
//         // 해당 인덱스를 제외한 나머지 문자열 
//         for(int i = 0; i < my_string.length(); i++) {
//             list.add(my_string.substring(i, my_string.length()));
//         }
//         list.sort(Comparator.naturalOrder());
//         return list;
//     }
// 

import java.util.*;
import java.util.stream.IntStream;

class Solution {
    public String[] solution(String myString) {
        return IntStream.range(0, myString.length()).mapToObj(myString::substring).sorted().toArray(String[]::new);
    }
}