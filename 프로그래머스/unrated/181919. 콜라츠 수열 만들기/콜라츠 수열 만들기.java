import java.util.ArrayList;
class Solution {
    public ArrayList<Integer> solution(int n) {            
        // 결과 초기화
        ArrayList<Integer> result = new ArrayList<Integer>();
        result.add(n);

        // 진행 순환
        while(n>1) {         
            // 짝수일때
            if(n%2 == 0) {
                n = n/2;
            }else{
                // 홀수일때
                n = (3*n) + 1;
            }
            result.add(n);
        }
        return result;
    }
}