import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<Integer>solution(int n, int k) {
        List<Integer> list = new ArrayList<>();
        int i = 1;
        while(i <= n) {
            // 순회로 도는 정수의 값이 k의 배수인 경우
            if(i%k == 0) {
                list.add(i);
            }
            i++;
        }
        return list;
    }
}