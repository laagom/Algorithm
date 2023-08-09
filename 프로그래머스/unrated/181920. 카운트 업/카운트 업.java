import java.util.ArrayList;
class Solution {
    public ArrayList<Integer> solution(int start, int end) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i = start; i <= end; i++){
            list.add(i);
        }
        return list;
    }
}