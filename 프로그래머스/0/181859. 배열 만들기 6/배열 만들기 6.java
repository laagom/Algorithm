import java.util.*;

class Solution {
    public List<Integer> solution(int[] arr) {
        int i = 0;
        List<Integer> stk = new ArrayList<Integer>();
        while(i < arr.length) {
            // stk가 빈 배열인 경우
            if(stk.size() == 0) {
                stk.add(arr[i]);
            // stk가 빈 배열이 아니며, stk의 마지막 원소가 arr[i]와 동일한 경우
            }else if(stk.size() != 0 && stk.get(stk.size()-1) == arr[i]) {
                stk.remove(stk.size()-1);
            // stk가 빈 배열이 아니며, stk의 마지막 원소가 arr[i]와 다른 경우
            }else if(stk.size() != 0 && stk.get(stk.size()-1) != arr[i]) {
                stk.add(arr[i]);
            }
            i++;
        }
        // stk가 빈 배열인 경우 -1이 담긴 배열 반환
        return stk.size() == 0 ? new ArrayList<Integer>(Arrays.asList(-1)) : stk;
    }
}