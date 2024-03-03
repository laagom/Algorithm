import java.util.List;
import java.util.ArrayList;
class Solution {
    public List<Integer> solution(int[] arr) {
        List<Integer> rtn = new ArrayList<Integer>();
        
        // 전달받은 원소 반복문 순회
        for(int i=0; i<arr.length; i++) {
            // 순회 도는 원소의 숫자 값
            int cnt = arr[i];
            
            // 원소의 숫자 값 만큼 반복문 순회하며 배열에 값 추가
            for(int j=0; j<cnt; j++)
                rtn.add(cnt);
        }
        return rtn;
    }
}