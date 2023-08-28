import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public String solution(String my_string, int[] index_list) {
        String answer = "";
        List<String> answerList = new ArrayList<String>();

        for(int i = 0; i < index_list.length; i++) {
            answerList.add(String.valueOf(my_string.charAt(index_list[i])));
        }

        return String.join("", answerList);
    }
}