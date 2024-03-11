import java.util.*;
class Solution {
    public String solution(String[] str_list, String ex) {
        String answer = "";
        System.out.println(String.join("", str_list));
        List<String> list = new ArrayList<String>();
        for(int i = 0; i < str_list.length; i++) {
            if(!str_list[i].contains(ex)) {
                list.add(str_list[i]);
            }
        }
        return String.join("", list);
    }
}