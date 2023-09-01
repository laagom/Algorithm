import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public final static int UPPER_START = 65;
    public final static int UPPER_END   = 90;
    public final static int LOWER_START = 97;
    public final static int LOWER_END   = 122;
    
    public int[] solution(String my_string) {     
        // 65~90, 97~122 총 52개
        int[] arr = new int[52];
        Arrays.setAll(arr, i -> 0);
        
        for(int i = 0; i < my_string.length(); i++) {
            // char형식을 아스키코드로 변경
            int index = (int)(my_string.charAt(i));
            
            // 대문자 65~90인 경우
            if(index >= UPPER_START && index <= UPPER_END) {
                arr[index-UPPER_START] += 1;
                
            // 소문자 97~122인 경우
            // 단 앞에 25개 대문자가 있으니 +26
            }else if(index >= LOWER_START && index <= LOWER_END) {
                arr[index-LOWER_START+26] += 1;
            }
        }   
        return arr;
    }
}