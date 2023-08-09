import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public List<Integer> solution(int l, int r) {
        List<Integer> result = new ArrayList<Integer>();
        
        for(int num = l; num <= r; num++) {        
            // 5로 나누어 떨어지지 않으면 넘김
            if(num%5 != 0){
                continue;
            }
            
            String num_word = String.valueOf(num);
            boolean five_and_zero = true;
            
            // 문자를 순회
            for(int i = 0; i < num_word.length(); i++) {
                char chr = num_word.charAt(i);
                // 문자 중 하나라도 0, 5가 아니면 false
                if(chr != '0' && chr != '5') {
                    five_and_zero = false;
                }
            }
            
            // 0, 5가 아닌 값이 없으면 결과
            if(five_and_zero) {
                result.add(Integer.valueOf(num_word));
            }
        }
        
        // 결과가 없으면 -1
        if(result.size() == 0){
            return Arrays.asList(-1);
        }
        
        return result;
    }
}