import java.util.List;
import java.util.ArrayList;

class Solution {
    public List solution(int[] num_list, int n) {
        List list = new ArrayList();
        int i = 0;
        for(int num : num_list) {
            if(i%n == 0) {
                list.add(num);
            }
            i++;
        }
        return list;
    }
}