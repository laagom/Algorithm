import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<Integer> solution(int start_num, int end_num) {
        List<Integer> answer = new ArrayList<Integer>();
        int loop_num = start_num;
        while(loop_num <= end_num) {
            answer.add(loop_num);
            loop_num++;
        }
        return answer;
    }
}