import java.util.Collections;
class Solution {
    public int solution(String[] strArr) {
        int answer = 0;
        int[] counts = new int[31];
        for(int i = 0; i < strArr.length; i++) {
            int len = strArr[i].length();
            counts[len] ++;
        }
        System.out.println(counts);
        
        return getMax(counts);
    }
    
    // 최대값 구하기
    public int getMax(int[] arr) {
        int max = 0;
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] >= max)
                max = arr[i];
        }
        return max;
    }
}