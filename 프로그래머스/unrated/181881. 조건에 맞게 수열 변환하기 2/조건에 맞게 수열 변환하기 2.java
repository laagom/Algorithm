import java.util.Arrays;

class Solution {
    public int solution(int[] arr) {  
        int res = 0;
        int convert_number = 0;
        int[] before_arr = arr.clone();
        
        // 이전 배열과 비교하여 동일할때 까지
        while(!Arrays.equals(arr, before_arr) || res == 0) {
            before_arr = arr.clone();
            res++;
            
            // 배열 순회
            for(int i = 0; i < arr.length; i++) {
                // 배열 변경 조건
                if(arr[i] >= 50 && arr[i]%2 == 0) {
                    convert_number = arr[i]/2;
                    
                }else if(arr[i] < 50 && arr[i]%2 == 1){
                    convert_number = arr[i]*2+1;
                    
                }else {
                    convert_number = arr[i];
                }

                // 배열 변경
                arr[i] = convert_number;
            }
        }
        
        return res-1;
    }
}