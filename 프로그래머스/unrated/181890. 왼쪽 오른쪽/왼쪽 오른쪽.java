import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public List<String> solution(String[] str_list) {
        boolean convert = true;
        String[] str = {"u", "d", "l", "r"};
            
        List<String> preList = new ArrayList<String>();
        List<String> nextList = new ArrayList<String>();
        int j = 0;
        for(int i = 0; i < str_list.length; i ++) {
            if(convert) {
                preList.add(str_list[i]);
            }else {
                nextList.add(str_list[i]);
            }
            
            // "l"이 처음 나오는 경우
            if(j == 0) {
                if(str[2].equals(str_list[i])) {
                preList.remove(preList.size()-1);
                j++;
                return preList;
                // "r"이 처음 나오는 경우
                }else if(str[3].equals(str_list[i])) {
                    convert = false;
                    j++;
                }   
            }
            
        }
        return nextList.size() != 0 ? nextList : new ArrayList<String>();
    }
}