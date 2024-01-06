import java.util.Arrays;

class Solution {
    public int solution(int[] num_list) {
        //[Stream]으로 연산하기
        
        // 리스트 길이가 11 이상인 경우
        if(num_list.length >= 11){ 
            return Arrays.stream(num_list).sum();
        }
        
        // 리스트 길이가 10 이하인 경우
        if(num_list.length <= 10){ 
            return Arrays.stream(num_list).reduce(1, (a, b) -> a*b); 
        }
        return 0;
    }
}