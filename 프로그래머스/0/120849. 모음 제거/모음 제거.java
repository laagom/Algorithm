import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
class Solution {
    public String solution(String my_string) {
        List<String> list = Arrays.asList("a", "e", "i", "o", "u");
        for(String str:list) my_string = my_string.replaceAll(str,"");
        return my_string;
    }
}