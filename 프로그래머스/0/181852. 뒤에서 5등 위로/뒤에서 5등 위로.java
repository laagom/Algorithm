import java.util.*;

class Solution {
    public List<Integer> solution(int[] num_list) {
        int temp = 0;
        List<Integer> answer = new ArrayList<Integer>();
        for(int i = 0; i < num_list.length; i++) {
            for(int j = 0; j < num_list.length; j++) {
                if(i!=j) {
                    if(num_list[i] < num_list[j]) {
                        temp = num_list[i];
                        num_list[i] = num_list[j];
                        num_list[j] = temp;
                    }  
                }
            }
        }
        
        for(int i = 5; i < num_list.length; i++)
            answer.add(num_list[i]);

        return answer;
    }
}