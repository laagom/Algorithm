import java.util.*;

class Solution {
    public static final int MAX_NUMBER = 1000000;
    public static final int SIZE_ZERO = -1;
    
    public List<Integer> solution(int[] arr, int[][] queries) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        ArrayList<Integer> list;   
        int s, e, k;
        
        for(int[] query:queries) {
            list = new ArrayList<Integer>();
            s = query[0];
            e = query[1];
            k = query[2];
            
            for(int i = s; i <= e; i++){
                if(arr[i] > k) {
                    list.add(Integer.valueOf(arr[i]));
                }
            }
            result.add(getMin(list));
        }  
        return result;
    }
    
    // 배열 최소값 구하기
    // 배열의 길이가 0 이면 -1 반환
    public int getMin(List<Integer> list) {
        int min_number = MAX_NUMBER;
        
        for(Integer number:list) {
            if(number < min_number) {
                min_number = number;
            }
        }    
        return min_number == MAX_NUMBER ? SIZE_ZERO : min_number;
    }
}