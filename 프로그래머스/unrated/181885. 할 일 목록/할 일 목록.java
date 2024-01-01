import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<String> solution(String[] todo_list, boolean[] finish_list) {
        List<String> list = new ArrayList<String>();
        
        for(int i = 0; i < todo_list.length; i++) {
            for(int j = 0; j < finish_list.length; j++) {
                if(i == j && finish_list[j] == false) {
                    list.add(todo_list[j]);
                }
            }
        }
        return list;
    }
}