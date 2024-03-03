import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<Integer> solution(int[] arr, boolean[] flag) {
        List<Integer> rtnList = new ArrayList<Integer>();
        
        // flag 배열 반복문 순회
        for(int i=0; i<flag.length; i++) {
            
            // flag = true인 경우
            if(flag[i]) {
                // arr[i]*2 만큼 arr[i]를 배열에 추가
                int cnt = arr[i]*2;
                for(int j=0; j<cnt; j++) {
                    rtnList.add(arr[i]);    
                }
            
            // flag = false인 경우
            }else {
                // arr[i] 만큼 마지막 배열에서 제거
                int cnt = arr[i];
                for(int j=0; j<cnt; j++) {
                    rtnList.remove(rtnList.size()-1);    
                }
            }
        }
        return rtnList;
    }
}