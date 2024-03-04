import java.util.*;

class Solution {
    public List<Integer> solution(int[] arr, int k) {
        List<Integer> result = new ArrayList<Integer>();
        
        // 랜덤으로 주어지는 배열을 반복문 순회
        for(int i=0; i<arr.length; i++) {
            int val = arr[i];
            
            // 배열이 K보다 작은경우
            if(k > result.size()) {
                // 랜덤으로 주어진 값이 포함이 되지 않은 경우
                if(!result.contains(val))
                    result.add(val);   
            }
            
            // 배열이 k와 동일한 사이즈가 된 경우 STOP
            if(result.size() == k)
                break;  
        }
        
        // k사이즈만큼 배열이 채워지지 않았다면
        if(k-result.size() != 0) {
            int cnt = k-result.size();
            // k사이즈 만큼 -1로 채워 넣는다.
            for(int i = 0; i < cnt; i++)
                result.add(-1);
        }
        return result;
    }
}