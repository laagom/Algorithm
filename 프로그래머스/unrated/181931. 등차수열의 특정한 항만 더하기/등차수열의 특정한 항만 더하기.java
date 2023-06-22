import java.util.ArrayList;
class Solution {
    public int solution(int a, int d, boolean[] included) {
        ArrayList<Integer> list = new ArrayList<>();     
        for(int i = 0;i < included.length; i++) {
            // System.out.println("i : " + i + "일때, boolean : " + included[i]);
            if(included[i]) { 
                list.add(a);
            }   
            a += d;
        }
        return list.stream().mapToInt(Integer::intValue).sum();
    }
}