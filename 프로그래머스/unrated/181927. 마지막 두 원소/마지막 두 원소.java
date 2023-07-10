import java.util.Arrays;
class Solution {
    public int[] solution(int[] num_list) {
        int[] answer    = Arrays.copyOf(num_list, num_list.length+1);  
        int last_num    = num_list[num_list.length-1];
        int forward_num = num_list[num_list.length-2];
        
        // 조건에 따른 마지막 인덱스
        if(last_num > forward_num) {
            answer[num_list.length] = last_num - forward_num;
        }else {
            answer[num_list.length] = last_num*2;
        }
        
        return answer;
    }
}